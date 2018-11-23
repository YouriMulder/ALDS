from ex_02 import myStack



def checkBrackets(bracketsString):
	pairs = [ ['(',')'], ['[',']'], ['<','>'] ] 
	
	mS = myStack()
	for index in range(len(bracketsString)):
		for pair in range(len(pairs)):
			
			if bracketsString[index] == pairs[pair][0]:
				mS.push(bracketsString[index])
			elif bracketsString[index] == pairs[pair][1]:
				if mS.pop() is not pairs[pair][0]:
					return False
		
	return True

# Allowed
correct_01 = "(((<>))())"
correct_02 = "[(<>)]()(()())"
correct_03 = "((<>))"

# Not allowed
not_correct_01 = "([)]"
not_correct_02 = "(((<)>))"

print(checkBrackets(correct_01))
print(checkBrackets(correct_02))
print(checkBrackets(correct_03))

print(checkBrackets(not_correct_01))
print(checkBrackets(not_correct_02))

