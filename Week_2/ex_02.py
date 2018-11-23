class myStack:
	def __init__(self):
		self.__elements = list()
	
	def push(self, element):
		self.__elements.append(element)
	
	def pop(self):
		if len(self.__elements) > 0:
			return self.__elements.pop()
		else:
			return None
	

	def peek(self):
		if len(self.__elements) > 0:
			return self.__elements.index(len(self.__elements) - 1)
		else:
			return None
	
	def isEmpty(self):
		return not len(self.__elements) > 0

"""
ms = myStack()
print(ms.peek())
print(ms.pop())

ms.push(111)
print(ms.pop())

while not ms.isEmpty():
	print(ms.pop())

ms.push(127)
print(ms.peek())
print(ms.pop())
"""






