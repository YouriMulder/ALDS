# Studentnumber : 1716390
# Class : V2C

class TrieWord:
	"""
	Constructor of the TrieWord class.

	Word is the value of the TrieNode.
	Frequency is the amount of times that word occurs in the Trie.
	"""
	def __init__(self, word, frequency):
		self.word = word
		self.frequency = frequency

class TrieNode:
	"""
	Constructor of the TrieNode class.

	Value is the value of the node in the Trie.
	Frequency is the amount of times that sequence of values occurs in the Trie.
	Childs is all the nodes under the current node.
	"""	
	def __init__(self, value=None, frequency=0, childs=[]):
		self.value = value
		self.frequency = frequency
		self.childs = childs


	"""
	Method to get a specific TrieNode using the value of the sequence of nodes.

	Parameters
	----------
	value : unknown
		The value you want to search in the tree.
		This is the whole sequence of nodes.

	valueIndex : integer 
		The current index in the value we want to check if it's the value of the node.

	Returns
	-------
	Child/None
		Returns a child when a child with the given sequence of the value is found.
		If not found the method returns None
	"""
	def getChildUsingValue(self, value, valueIndex):
		if valueIndex < len(value):
			for child in self.childs:
				if child.value == value[valueIndex]:
					return child

		return None

		"""
	Method to add a new child to the node.

	Parameters
	----------
	child : TrieNode
		The TrieNode you want to add to the childs of this TrieNode.

	Returns
	-------
	None
	"""
	def addChild(self, child):
		self.childs.append(child)

		"""
	Method to get a specific TrieNode using the value of the sequence of nodes.

	Parameters
	----------
	value : unknown
		The value you want to search in the tree.
		This is the whole sequence of nodes.

	valueIndex : integer 
		The current index in the value we want to check if it's the value of the node.

	Returns
	-------
	Child/None
		Returns a child when a child with the given sequence of the value is found.
		
	def insert(self, value, valueIndex=0):
		if valueIndex == len(value):
			self.frequency += 1
			return True

		child = self.getChildUsingValue(value, valueIndex)
		if child:
			child.insert(value, valueIndex + 1)
		else:
			newChild = TrieNode(value[valueIndex], 0 , [])
			self.addChild(newChild)
			newChild.insert(value, valueIndex + 1)

	def search(self, value, valueIndex=0):
		if valueIndex == len(value):
			return self

		child = self.getChildUsingValue(value, valueIndex)
		if child:
			return child.search(value, valueIndex + 1)
		else:
			return None

	def printWords(self, word=[], woorden=[]):
		if self.value != None:
			word.append(self.value)
		if self.frequency:
			woorden.append(TrieWord(''.join(word), self.frequency))
		
		if self.childs:
			for child in self.childs:
				child.printWords(word)
				word.pop()

		return woorden

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, value):
		value = value.lower()
		self.root.insert(value)

	def search(self, value):
		value = value.lower()		
		return self.root.search(value)

	def print(self):
		return self.root.printWords()

	def addWordsFromFile(self, inputFile):
		inputFile = open(inputFile, "r")
		text = inputFile.readlines()
		inputFile.close()
		text = ''.join(text)


		startWordIndex = 0
		endWordIndex = 0
		currentIndex = 0
		while currentIndex < len(text):
			currentCharacter = text[currentIndex]
			if not currentCharacter.isalpha():
				endWordIndex = currentIndex
				word = text[startWordIndex : endWordIndex].lower()
				
				self.insert(word)
				
				while currentIndex < len(text) and not text[currentIndex].isalpha():
					currentIndex += 1

				startWordIndex = currentIndex
			currentIndex += 1

	
	def exportTreeToFile(self, outputFile):
		outputFile = open(outputFile, "w")
		words = self.print()
		for trieWord in words:
			outputFile.write(str(trieWord.word) + " " + str(trieWord.frequency) + "\n")
		outputFile.close()


if __name__ == "__main__":	
	boompie = Trie()
	boompie.insert("Test")
	boompie.insert("test2")
	boompie.insert("appelaaneenstok")