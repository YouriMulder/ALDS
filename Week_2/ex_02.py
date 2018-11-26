# Studentnumber : 1716390
# Class : V2C

class myStack:
	"""
	Class constructor
	"""
	def __init__(self):
		self.__elements = list()
	
	"""
	Method to push a element to the back of the stack.
	
	Parameters
	----------
	element : unknown
		The element you want to push to the stack.
	"""
	def push(self, element):
		self.__elements.append(element)
	
	"""
	Method to pop the last added item in the stack if there is one.
	This item will be deleted when returned.

	Returns
	-------
	Unknown:
		This will be the last added element on the stack.
		If the stack is empty the method will return None.
	"""
	def pop(self):
		if len(self.__elements) > 0:
			return self.__elements.pop()
		else:
			return None
	
	"""
	Method used to return the last added item on the stack.
	This item will not be deleted.

	Returns
	-------
	Unknown:
		This will be the last element on the stack.
		If the stack is empty the method will return None.
	"""
	def peek(self):
		if len(self.__elements) > 0:
			return self.__elements[len(self.__elements) - 1]
		else:
			return None

	
	"""
	Method used to check if the stack is empty.

	Returns
	-------
	Boolean:
		This boolean will be True when the stack is empty 
		and False if it contains at least one item.
	"""
	def isEmpty(self):
		return not len(self.__elements) > 0

if __name__ == "__main__":	
	testStack = myStack()
	print(testStack.peek())
	print(testStack.pop())

	testStack.push(111)
	print(testStack.pop())

	while not testStack.isEmpty():
		print(testStack.pop())

	testStack.push(127)
	print(testStack.peek())
	print(testStack.pop())

	testStack.push("test string")
	testStack.push([13,23])
	print(testStack.peek())
	print(testStack.pop())
	print(testStack.pop())
