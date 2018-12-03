class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
# FiFo
class Queue:
	def __init__(self):
		self.startPointer = None
		self.endPointer = None

	def enqueue(self, value):
		if self.startPointer is None:
			newStart = Node(value)
			self.startPointer = newStart
			self.endPointer = newStart
		else:
			newEnd = Node(value)
			self.endPointer.next = newEnd
			self.endPointer = newEnd



	def dequeue(self):
		if self.startPointer is None:
			return None

		print("start: ", self.startPointer.value)
		print("end: ", self.endPointer.value)
		
		temp = self.startPointer

		self.startPointer = self.startPointer.next

		if self.startPointer is None:
			self.endPointer = None

		return temp.value


testQueue = Queue()

for x in range(10):
	testQueue.enqueue(x)

print(testQueue.startPointer.value)
print(testQueue.startPointer.next.value)
print(testQueue.startPointer.next.next.value)


print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())

print(testQueue.startPointer)
print(testQueue.endPointer)

testQueue.enqueue(100)
print(testQueue.startPointer)
print(testQueue.endPointer)
print(testQueue.dequeue())

print(testQueue.startPointer)
print(testQueue.endPointer)