
def getDependency(token):
	while token.head.dep_ != "ROOT":
		token = token.head
	return token.dep_

def getHead(token):
	while token.head.dep_ != "ROOT":
		token = token.head
	return token
