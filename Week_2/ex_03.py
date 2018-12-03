# Studentnumber : 1716390
# Class : V2C

from ex_02 import myStack

"""
Function to check whether 
the amount of closing and opening brackets 
in a given string match.

Parameters
----------
bracketsString:
	The string you want to check the amount of brackets of.
	Only () [] and <> are allowed in this string.

Returns
-------
Boolean:
	This boolean will be True when the amount of brackets match 
	and False if they do not match.
	
"""
def checkBrackets(bracketsString):
	pairs = [ ['(',')'], ['[',']'], ['<','>'] ] 
	
	mS = myStack()
	for index in range(len(bracketsString)):
		if bracketsString[index] not in pairs[0] + pairs[1] + pairs[2]:
			return False

		for pair in range(len(pairs)):
			
			if bracketsString[index] == pairs[pair][0]:
				mS.push(bracketsString[index])
			elif bracketsString[index] == pairs[pair][1]:
				if mS.pop() is not pairs[pair][0]:
					return False

	if not mS.isEmpty():
		return False
	return True

if __name__ == "__main__":
	# Allowed
	testStrings = list()
	testStrings.append("(((<>))())")
	testStrings.append("[(<>)]()(()())")
	testStrings.append("((<>))")
	testStrings.append("([])")

	# Not allowed
	testStrings.append("([)]")
	testStrings.append("(((<)>))")
	testStrings.append("[](()][]])")
	testStrings.append("()()[][a[]]")
	testStrings.append("(])[")
	testStrings.append("()[]{}")
	testStrings.append(")([]")
	testStrings.append("(()")

	for testString in testStrings:
		print(checkBrackets(testString))
