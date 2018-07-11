import spacy
from element import *
from readFiles import *

print("Loading spacy...")
nlp = spacy.load("en")
print("Done")
print("Loading parsings...")
readParsings()
while True:
	s = input()
	t = input()
	tokens = nlp(s)
	e = Element()
	e.tokenList = tokens
	e.elementType = t
	e.createParsings()
	print(c.parsings)
