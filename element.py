class Element(object):
	elementType = "entity"
	characteristics =  {"length": 20, "begin": 2}

	tokenList = []

	parsings = []

	def __init__():
		pass

	def createParsingsHelper2(orderedPair, tokens, protoelement):
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
					parsings = createParsingsHelper(orderedPair, tokens)
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
			parsings = createParsingsHelper(orderedPair, tokens)
			for p in parsings:
				p.elements = [element] + p.elements
			returnList += parsings
		return returnList
				

	def createParsingsHelper(orderedPair, tokens):
		#base case
		if orderedPair.orderedList == [] and orderedPair.unorderedList == [] and tokens = []:
			parsing = Parsing()
			return [parsing]
		if orderedPair.orderedList == [] and orderedPair.unorderedList == [] or tokens = []:
			return []

		returnList = []
		element = orderedPair.orderedList[0]
		op = OrderedPair()
		op.orderedList = orderedPair.orderedList.copy().remove(element)
		op.unorderedList = orderedPair.unorderedList.copy()
		returnList += createParsingsHelper2(op, tokens, element)

		for element in orderedPair.unorderedList.copy():
			op = OrderedPair()
			op.orderedList = orderedPair.orderedList.copy().remove(element)
			op.unorderedList = orderedPair.unorderedList.copy()
			returnList += createParsingsHelper2(op, tokens, element)

	def createParsings():
		if not self.elementType in protoParsings:
			print("ElementType not supported by the ltp files: " + self.elementType)

		parsings = []
		for p in protoParsings[self.elementType]:
			for c in createParsingsHelper(p.op, tokens):
				c.code = p.code.copy()
				parsings.append(c)
		self.parsings = parsings
		pass

	def getStatements():
		pass
