import random

# Hoeveelheid vergelijkingen: n - 1, bij 10'000 dus 9999
# Hoevaak worden ze vergeleken 
# bij worst case scenario pivot is lowestIndex:  

class quickSort:
	def __init__(self, unsortedList):
		assert len(unsortedList) > 0
		self.counter = 0
		self.quickSortList = unsortedList

	def swap(self, initialList, firstIndex, secondIndex):
		temp = initialList[secondIndex]
		initialList[secondIndex] = initialList[firstIndex]
		initialList[firstIndex] = temp

	def startSort(self):
		self.counter = 0
		self.quickSort(self.quickSortList, 0, len(self.quickSortList) - 1)

	def quickSort(self, quickSortList, lowIndex, highIndex):
		if(lowIndex >= highIndex):
			return quickSortList

		pivotIndex = lowIndex
		#pivotIndex = int((lowIndex + highIndex) / 2)
		newPivotIndex = self.partition(quickSortList, lowIndex, highIndex, quickSortList[pivotIndex])
		# sort the left side of the pivot
		self.quickSort(quickSortList, lowIndex, newPivotIndex -1)
		# sort the right side
		self.quickSort(quickSortList, newPivotIndex, highIndex)


	def partition(self, quickSortList, lowIndex, highIndex, pivotValue):
		self.counter += 1		
		while(lowIndex <= highIndex):
			while(quickSortList[lowIndex] < pivotValue):
				lowIndex += 1
				self.counter += 1
			while(quickSortList[highIndex] > pivotValue):
				highIndex -= 1
				self.counter += 1

			if(lowIndex <= highIndex):
				self.swap(quickSortList, lowIndex, highIndex)
				lowIndex += 1
				highIndex -= 1
		
		# new index of the pivot
		return lowIndex

amountOfListElements = 10000
unsortedList = [random.randrange(1, amountOfListElements * 2, 1) for _ in range(amountOfListElements)]
qs = quickSort(unsortedList)

qs.startSort()

for i in range(len(qs.quickSortList) - 2):
	if not qs.quickSortList[i] <= qs.quickSortList[i]:
		print("not sorted")

print(qs.counter)
