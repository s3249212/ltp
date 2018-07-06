#def Read(object):
import os

#protoParsings = {"entity": [parsing1, parsing2], "attr": [parsing3, parsing4]}
protoParsings = {}

#TODO: create StringIterator.

whitespaces = [" ", "\t", "\n"]

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

def parseString(endingCharacter): #TODO: make this dependant on the element type such that you can say [entity key=value] without the final whitespace. ([entity key=value ]) as well as for the "=" sign (key=value)
	string = ""

	if stringIterator.hasNext() == False:
		return ""

	c = stringIterator.getNext()
	if c == '"' or c == "'": # or c == "'''":
		quoted = True
		quotationmark = c
	else:
		quoted = False
	
	while True:
		if stringIterator.hasNext() == False:
			return "" #raise ParsingError

		c = stringIterator.getNext()
		if quoted == True and c == quotationmark or quoted == False and (c in whitespaces or c == endingCharacter):
			return string
		else:
			string += c

def parseKeyValuePair():
	stringIterator.skipWhites()
	key = parseString()
	if parse("=") == False:
		return []
	value = parseString()
	return (key, value)
	
def parseElement():
	protoElement = ProtoElement()
	stringIterator.skipWhites()
	protoElement.type = parseString();
	stringIterator.skipWhites()
	(key, value) = parseKeyValuePair()
	protoElement.characteristics[key] = value

def parseScheme():
	if parse("{") == False:
		raise ParsingError

	level = 0
	stringIterator.skipWhites()
	if stringIterator.hasNext() == False:
		return [] #raise ParsingError unexpected end of file
	c = stringIterator.getNext()

	if c == "[":
		op.ordered.append(parseElement("]"))
	elif c == "<":
		op.unordered.append(parseElement(">"))
	else:
		raise ParsingError #unexpected element type

def getParsings(string): #TODO: make this a loop to go through all parsings in the file. As well as give an error as to what part of the program gave an error. The error must be given when an unexpected character occured and must print that to the screen and exit the program, without adding to much "raise ValueError"s and error cascading.
	#protoParsing[type] = parsing
	level = 0
	stringIterator.skipWhites()
	if stringIterator.hasNext() == False:
		return [] #raise ParsingError
	c = stringIterator.getNext()
	if c != "{":
		return []
	stringIterator.skipWhites()
	if stringIterator.hasNext() == False:
		return [] #raise ParsingError
	c = stringIterator.getNext()
	if c == "["
	pass

#for each ltp file, read all parsings (scheme, code, probability)

def readParsings():
	ltpfiles = getLTPFiles()
	for f in ltpfiles:
		F = open(f, "r")
		string = F.read()
		base = os.path.basename(f)
		type = os.path.splitext(base)[0]
		if type in protoParsings:
			pass
		protoParsings[type] = getParsings(string)
		F.close()

readParsings()
print(getLTPFiles())
print(protoParsings)

