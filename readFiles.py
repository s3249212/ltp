#def Read(object):
import os
from stringIterator import StringIterator
from parsingError import *
from orderedPair import *
from protoElement import *
from protoParsing import *
from spacyFunctions import *
#protoParsings = {"entity": [parsing1, parsing2], "attr": [parsing3, parsing4]}
protoParsings = {}

#TODO: create StringIterator.

whitespaces = [" ", "\t", "\n"]
stringIterator = None
i = 0

def getLTPFiles():
	filenames = []
	if os.path.isdir("./parsingSchemes") == False:
		return []

	for file in os.listdir("./parsingSchemes"):
		if file.endswith(".ltp"):
			filenames.append(os.path.join("./parsingSchemes", file))
	return filenames

def parse(c):
	if stringIterator.hasNext() == False:
		return False

	c2 = stringIterator.getNext()
	return c == c2

def parsePeek(c):
	if stringIterator.hasNext() == False:
		return False

	c2 = stringIterator.peek()
	return c == c2

def parseString(endingCharacter): #TODO: make this dependant on the element type such that you can say [entity key=value] without the final whitespace. ([entity key=value ]) as well as for the "=" sign (key=value)
	string = ""

	global i
	i += 1
	#print(i)
	if stringIterator.hasNext() == False:
		raise ParsingError #return ""

	c = stringIterator.peek()
	if c == '"' or c == "'": # or c == "'''":
		quoted = True
		quotationmark = c
		stringIterator.getNext()
	else:
		quoted = False
	
	while True:
		if stringIterator.hasNext() == False:
			raise ParsingError #return "" #raise ParsingError

		c = stringIterator.peek()
		if quoted == False and c == endingCharacter:
			#print(string)
			return string

		stringIterator.getNext()
		if quoted == True and c == quotationmark or quoted == False and c in whitespaces:
			#print(string)
			return string
		else:
			string += c

def parseKeyValuePair(endCharacter):
	stringIterator.skipWhites()
	key = parseString("=")
	if parse("=") == False:
		return (1,1) #raise ParsingError
	value = parseString(endCharacter)
	return (key, value)
	
def parseElement(endCharacter):
	stringIterator.skipWhites()
	if parsePeek("{"):
		protoElement = parseScheme()
	else:
		protoElement = ProtoElement()
		stringIterator.skipWhites()
		protoElement.type = parseString(endCharacter)
		while stringIterator.peek() != endCharacter:
			stringIterator.skipWhites()
			(key, value) = parseKeyValuePair(endCharacter)
			protoElement.characteristics[key] = value
			stringIterator.skipWhites()
		stringIterator.getNext()
	return protoElement
	

def parseScheme():
	if parse("{") == False:
		raise ParsingError

	level = 0
	op = OrderedPair()
	#print(len(op.orderedList))
	#for o in op.orderedList:
	#	print(o.type)
	stringIterator.skipWhites()
	while stringIterator.peek() != "}":
		if stringIterator.hasNext() == False:
			raise ParsingError #unexpected end of file
		c = stringIterator.getNext()
		if c == "[":
			op.orderedList.append(parseElement("]"))
		elif c == "<":
			op.unorderedList.append(parseElement(">"))
		else:
			raise ParsingError #unexpected element type
		#for o in op.orderedList:
		#	print("o characteristics: "+str(o.characteristics))
		stringIterator.skipWhites()
	stringIterator.getNext()
	return op

def parseCode():
	if parse("{") == False:
		raise ParsingError

	code = parseString("}")

	if parse("}") == False:
		raise ParsingError

	return code

def getParsings(string): #TODO: make this a loop to go through all parsings in the file. As well as give an error as to what part of the program gave an error. The error must be given when an unexpected character occured and must print that to the screen and exit the program, without adding to much "raise ValueError"s and error cascading.
	#protoParsing[type] = parsing
	#print(string)
	level = 0
	global stringIterator
	stringIterator = StringIterator(string)
	#print(stringIterator.string)
	parsings = []
	stringIterator.skipWhites()
	while stringIterator.hasNext():
		parsing = ProtoParsing()
		parsing.op = parseScheme()
		stringIterator.skipWhites()
		parsing.code = parseCode()
		stringIterator.skipWhites()
		parsings.append(parsing)
	return parsings
	#if stringIterator.hasNext() == False:
	#	return [] #raise ParsingError
	#c = stringIterator.getNext()
	#if c != "{":
	#	return []
	#stringIterator.skipWhites()
	#if stringIterator.hasNext() == False:
	#	return [] #raise ParsingError
	#c = stringIterator.getNext()
	#if c == "["
	#pass

#for each ltp file, read all parsings (scheme, code, probability)

def getProtoParsings():
	global protoParsings
	return protoParsings

def readParsings():
	ltpfiles = getLTPFiles()
	for f in ltpfiles:
		F = open(f, "r")
		string = F.read()
		base = os.path.basename(f)
		type = os.path.splitext(base)[0]
		if type in protoParsings:
			pass
		#print(type)
		protoParsings[type] = getParsings(string)
		F.close()

def printParsings():
	for k, v in protoParsings.items():
		print(k)
		for p in v:
			print("\tOrderedList:")
			for o in p.op.orderedList:
				print("\t\t"+o.type)
				for a, b in o.characteristics.items():
					print("\t\t"+a + ": " + b)
		
			print("\tUnorderedList:")
			for o in p.op.unorderedList:
				print("\t\t"+o.type)
				for a, b in o.characteristics.items():
					print("\t\t"+a + ": " + b)
#readParsings()
#printParsings()
#print(getLTPFiles())
#print(protoParsings["entity"][0].op.orderedList[0].type)
#print(protoParsings)

