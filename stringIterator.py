whitespaces = [" ", "\t", "\n"]

class StringIterator(object):
	string = ""
	size = len(string)
	i = -1
	
	def __init__(string):
		self.string = string

	def peek():
		if hasNext() == False:
			return ""
		return string[i + 1]

	def hasNext():
		return i + 1 < size

	def getNext():
		c = string[i + 1]
		i += 1
		return c

	def getCurrent():
		c = string[i]

	def skipWhites():
		while hasNext() and peek() in whitespaces:
			i += 1

