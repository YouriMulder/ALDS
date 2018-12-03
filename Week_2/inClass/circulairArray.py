class circulairArray():
	
	def __init__(self, size):
		self.lst = list()
		self.size = size
		self.popPointer = 0
		self.insertPointer = 0

	def enqueue(self, e):
		print(self.insertPointer % (self.size - 1), self.popPointer % (self.size - 1))
		if self.insertPointer % self.size - 1 >= self.popPointer % self.size - 1: 
			self.lst.insert(self.insertPointer % self.size, e)
			self.insertPointer += 1

	def denqueue(self):
		if self.insertPointer == 0 or self.popPointer == self.insertPointer - 1:
			return None
		
		self.popPointer += 1
		return self.lst[self.popPointer % self.size - 1]

	def print(self):
		for index in range(self.popPointer, self.insertPointer):
			#print(self.lst[index])
			pass

ca = circulairArray(10)

for i in range(10):
	ca.enqueue(i)
	ca.print()
	print("---")

print(ca.denqueue())
print(ca.denqueue())
print("end")

for i in range(20,30):
	ca.enqueue(i)
	ca.print()
	print("---")

print(ca.denqueue())
print(ca.denqueue())

