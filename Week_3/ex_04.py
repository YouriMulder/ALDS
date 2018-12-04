# Studentnumber : 1716390
# Class : V2C

from trie import Trie
from trie import TrieNode

"""
Function used to transform a list of word into a dictonary with the frequency of the words.

Parameters
----------
text : str
	The text you want to get the frequency of the words of.

Returns
-------
None
"""
def getDictOfWords(text):
	words = dict()
	startWordIndex = 0
	endWordIndex = 0
	currentIndex = 0
	while currentIndex < len(text):
		currentCharacter = text[currentIndex]
		if not currentCharacter.isalpha():
			endWordIndex = currentIndex
			word = text[startWordIndex : endWordIndex].lower()
			if word in words:
				words[word] = words[word] + 1
			else:
				words[word] = 1

			while currentIndex < len(text) and not text[currentIndex].isalpha():
				currentIndex += 1

			startWordIndex = currentIndex
		currentIndex += 1
	return words


"""
Function to write the output of get DictOfWords to a given file.

Parameters
----------
inputFile : str
	The file you want to get the frequency of the words of.


outputFile : str
	The file you want to write the output of DictOfWords to.

Returns
-------
boolean
    Boolean containing True when the position is possible.
    If not possible the boolean contains False.
"""
def wordCountToFileUsingDict(inputFile, outputFile):
	inputFile = open(inputFile, "r")
	text = inputFile.readlines()
	inputFile.close()

	words = getDictOfWords(''.join(text))
	outputFile = open(outputFile, "w")
	for key, value in words.items():
		outputFile.write(str(key) + " " + str(value) + "\n")
	outputFile.close()

"""
Function to write the output of a datastructure trie 
with all the words from a file to a given file.

Parameters
----------
inputFile : str
	The file you want to get the frequency of the words of.


outputFile : str
	The file you want to write the output of DictOfWords to.

Returns
-------
boolean
    Boolean containing True when the position is possible.
    If not possible the boolean contains False.
"""
def wordCountToFileUsingTrie(inputFile, outputFile):
	inputFile = open(inputFile, "r")
	text = inputFile.readlines()
	inputFile.close()

	words = getDictOfWords(''.join(text))
	outputFile = open(outputFile, "w")
	for key, value in words.items():
		outputFile.write(str(key) + " " + str(value) + "\n")
	outputFile.close()

if __name__ == "__main__":
	wordCountToFileUsingDict("inputText.txt", "outputDictWords.txt")
	
	tree = Trie()
	tree.addWordsFromFile("inputText.txt")
	tree.exportTreeToFile("outputTrieWords.txt")
	