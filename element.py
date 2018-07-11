from readFiles import *
class Element(object):
	def __init__(self):
		self.elementType = ""
		self.characteristics =  {}

		self.tokenList = []

		self.parsings = []

	def createParsingsHelper2(self, orderedPair, tokens, protoelement):
		returnList = []
		element = Element()
		element.characteristics = protoelement.characteristics.copy()
		if "dep" in protoelement.characteristics:
			if getDependency(tokens[0]) == protoelement.characteristics["dep"]:
				bool = True
				for t in getHead(tokens[0]).subtree:
					bool = bool and t in tokens
					tokens.remove(t)
					element.tokenList.append(t)
				if bool:
					parsings = self.createParsingsHelper(orderedPair, tokens)
					for p in parsings:
						p.elements = [element] + p.elements
					return parsings
		
		for t in tokens:
			newTokens = tokens.copy()
			elementTokens = []
			for n in newTokens:
				elementTokens.append(n)
				newTokens.remove(n)
				if t == n:
					break
			element = Element()
			element.characteristics = protoelement.characteristics.copy()
			parsings = self.createParsingsHelper(orderedPair, tokens)
			for p in parsings:
				p.elements = [element] + p.elements
			returnList += parsings
		return returnList
				

	def createParsingsHelper(self, orderedPair, tokens):
		#base case
		print("")
		print(orderedPair.orderedList)
		print(orderedPair.unorderedList)
		print(tokens)
		print("")
		if orderedPair.orderedList == [] and orderedPair.unorderedList == [] and tokens == []:
			parsing = Parsing()
			return [parsing]
		if orderedPair.orderedList == [] and orderedPair.unorderedList == [] or tokens == []:
			return []

		returnList = []
		#print("Ordered pair")
		#print(orderedPair)
		element = orderedPair.orderedList[0]
		op = OrderedPair()
		op.orderedList = orderedPair.orderedList.copy()
		op.orderedList.remove(element)
		op.unorderedList = orderedPair.unorderedList.copy()
		returnList += self.createParsingsHelper2(op, tokens, element)

		for element in orderedPair.unorderedList.copy():
			op = OrderedPair()
			op.orderedList = orderedPair.orderedList.copy().remove(element)
			op.unorderedList = orderedPair.unorderedList.copy()
			op.unorderedList.remove(element)
			returnList += self.createParsingsHelper2(op, tokens, element)
		return returnList

	def createParsings(self):
		if not self.elementType in protoParsings:
			print("ElementType not supported by the ltp files: " + self.elementType)

		parsings = []
		#tokens = nlp(self.tokenList)
		tokens = [t for t in self.tokenList]
		for p in getProtoParsings()[self.elementType]:
			for c in self.createParsingsHelper(p.op, tokens):
				c.code = p.code.copy()
				parsings.append(c)
		self.parsings = parsings
		pass

	def getStatements(self):
		pass
