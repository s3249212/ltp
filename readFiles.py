#def Read(object):
import os

#protoParsings = {"entity": [parsing1, parsing2], "attr": [parsing3, parsing4]}
protoParsings = {}

def getLTPFiles():
	filenames = []
	if os.path.isdir("./parsingSchemes") == False:
		return []

	for file in os.listdir("./parsingSchemes"):
		if file.endswith(".ltp"):
			filenames.append(os.path.join("./parsingSchemes", file))
	return filenames

def getParsings(string):
	#protoParsing[type] = parsing
	pass

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

