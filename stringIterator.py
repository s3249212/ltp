import sys
whitespaces = [" ", "\t", "\n"]

class StringIterator(object):
	def __init__(self, string):
		self.string = string
		self.size = len(string)
		self.i = -1
		#print(string + " " + str(self.size))

	def peek(self):
		if self.hasNext() == False:
			return ""
		return self.string[self.i + 1]

	def hasNext(self):
		#print(str(self.i) + " " + str(self.size))
		#print("self.string: "+self.string)
		return self.i + 1 < self.size

	def getNext(self):
		c = self.string[self.i + 1]
		self.i += 1
		#print("c: "+c)
		return c

	def getCurrent(self):
		return self.string[self.i]

	def skipWhites(self):
		while self.hasNext() and self.peek() in whitespaces:
			self.i += 1
			#print(self.i)

