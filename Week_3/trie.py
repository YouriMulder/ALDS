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
		The value you want to insert in the tree.
		This is the whole sequence of nodes.

	valueIndex : integer 
		The current index in the value we want to check if it's the value of the node.

	Returns
	-------
	Boolean
		Returns True a sequence of nodes is found containing the given value.
	"""
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


	"""
	Method to search a TrieNode using the value of the sequence of nodes.

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
	"""
	def search(self, value, valueIndex=0):
		if valueIndex == len(value):
			return self

		child = self.getChildUsingValue(value, valueIndex)
		if child:
			return child.search(value, valueIndex + 1)
		else:
			return None

	"""
	Method to get all the words with their frequency in the Trie.

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
	"""
	def getWords(self, word=[], words=[]):
		if self.value != None:
			word.append(self.value)
		if self.frequency:
			words.append(TrieWord(''.join(word), self.frequency))
		
		if self.childs:
			for child in self.childs:
				child.getWords(word)
				word.pop()

		return words

class Trie:
	"""
	Constructor of the Trie class.

	Root is the root of the Trie
	"""	
	def __init__(self):
		self.root = TrieNode()

	"""
	Method to insert a new value into the Trie.

	Parameters
	----------
	value : unknown
		The value you want to insert in the tree.
		This is the whole sequence of nodes.

	Returns
	-------
	None
	"""
	def insert(self, value):
		value = value.lower()
		self.root.insert(value)

	"""
	Method to search a TrieNode using the value of the sequence of nodes.

	Parameters
	----------
	value : unknown
		The value you want to search in the tree.
		This is the whole sequence of nodes.

	Returns
	-------
	TrieNode/None
		Returns a TrieNode when the value has been found. Otherwise it will return None.
	"""
	def search(self, value):
		value = value.lower()		
		return self.root.search(value)

	"""
	Method to get all the words and frequencies in a Trie.

	Returns
	-------
	list
		Returns a list of TrieWords.
	"""
	def getWords(self):
		return self.root.getWords()

	"""
	Method to add all the words to the tree from a given file.

	Parameters
	----------
	inputFile : str
		The inputFile is the path to the file where you want to get all the words of.

	Returns
	-------
	None
	"""
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

	"""
	Method to export all the words with their frequencies to a file.

	Parameters
	----------
	outputFile : str
		The outputFile is the path to the file where you want to store all the words and frequencies.

	Returns
	-------
	Child/None
		Returns a child when a child with the given sequence of the value is found.
	"""
	def exportTreeToFile(self, outputFile):
		outputFile = open(outputFile, "w")
		words = self.getWords()
		for trieWord in words:
			outputFile.write(str(trieWord.word) + " " + str(trieWord.frequency) + "\n")
		outputFile.close()


if __name__ == "__main__":	
	boompie = Trie()
	boompie.insert("Test")
	boompie.insert("test2")
	boompie.insert("appelaaneenstok")