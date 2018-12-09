class SepChainHash():

	def __init__(self, initialLength = 10):
		self.elements = [None] * initialLength
		self.elementsLength = initialLength
		self.amountOfElements = 0

	def __str__(self):
		return str(self.elements)

	def indexFromValue(self, value):
		return hash(value) % self.elementsLength

	def search(self, value):
		searchResult = self.elements[self.indexFromValue(value)]
		if searchResult:
			return value in searchResult 

		return False


	def checkLoadFactor(self):
		self.loadFactor = self.amountOfElements / self.elementsLength
		if(self.loadFactor > 0.75):
			self.rehash(self.elementsLength * 2)

	def insert(self, value):
		hashIndex = self.indexFromValue(value)

		if self.elements[hashIndex]:
			if not self.elements[hashIndex].add(value):
				return False
		else:
			self.elements[hashIndex] = {value}

		self.amountOfElements += 1
		self.checkLoadFactor()
		return True

	def delete(self, value):
		hashIndex = self.indexFromValue(value)

		if value in self.elements[hashIndex]:
			self.elements[hashIndex].remove(value)
			self.amountOfElements -= 1
			if len(self.elements[hashIndex]) == 0:
				self.elements[hashIndex] = None
			return True
		
		return False

	def rehash(self, newLen):
		temp = self.elements
		self.elementsLength = newLen
		self.elements = [None] * self.elementsLength
		
		for elementSet in temp:
			if elementSet:
				for element in elementSet:
					self.insert(element)

		print()
		print("Rehashed: ")
		print(str(self))
		print()



hashTest = SepChainHash()

for i in range(5):
	hashTest.insert(i)

hashTest.insert(11)
hashTest.insert(13)

print(hashTest)

for i in range(20):
	hashTest.insert(i)

hashTest.insert(20202002)
hashTest.insert("test")

print(hashTest)
print()

hashTest.delete(17)
print(hashTest)
print()

hashTest.delete(2)
print(hashTest)
print()
	
hashTest.insert(1010101010)
print(hashTest)
print()

hashTest = SepChainHash()

for i in range(100):
	hashTest.insert(random.random)

