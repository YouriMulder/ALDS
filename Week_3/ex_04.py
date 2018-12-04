# Studentnumber : 1716390
# Class : V2C

from trie import Trie
from trie import TrieNode

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


def wordCountToFileUsingDict(inputFile, outputFile):
	inputFile = open(inputFile, "r")
	text = inputFile.readlines()
	inputFile.close()

	words = getDictOfWords(''.join(text))
	outputFile = open(outputFile, "w")
	for key, value in words.items():
		outputFile.write(str(key) + " " + str(value) + "\n")
	outputFile.close()

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
	