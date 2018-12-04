# Studentnumber : 1716390
# Class : V2C

class Queue(list):
	def __init__(self, elements=[]):
		list.__init__(self, elements)
	
	def dequeue(self):
		return self.pop(0)
	
	def enqueue(self, value):
		self.append(value)

testQueue = Queue([3,4,5])

print("q: ", testQueue)

testQueue.enqueue(100)
print("q: ", testQueue)

print("dequeue: ", testQueue.dequeue())
print("q: ", testQueue)

print("dequeue: ", testQueue.dequeue())
print("q: ", testQueue)
