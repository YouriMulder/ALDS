import random
import sys

class quickSort:

	"""
	Constructor of the quickSort class.

	Parameters
	----------
	unsortedList : list:
		This list contains the values you want to quicksort.
	"""
	def __init__(self, unsortedList):
		assert len(unsortedList) > 0
		self.counter = 0
		self.quickSortList = unsortedList
	
	"""
	Function to swap two values in a array using indices.
	
	Parameters
	----------
	initialList : list
		This list you want to swap the indices of.

	firstIndex : integer
		The index of the first element you want to swap.
	
	secondIndex : integer
		The index of the second element you want to swap.	
	"""
	def swap(self, initialList, firstIndex, secondIndex):
		temp = initialList[secondIndex]
		initialList[secondIndex] = initialList[firstIndex]
		initialList[firstIndex] = temp

	"""
	Start the quicksort algorithm.		
	"""
	def startSort(self):
		self.counter = 0
		self.quickSort(self.quickSortList)


	"""
	Method used to quicksort a list using recusion.

	Parameters
	----------
	quickSortList : List
		The list you want to quickSort. 

	lowIndex: Integer
		The lowest index of the list.
		In the recusion process this will be the lowest index of the subList.

	highIndex: Integer
		The highest index of the list.
		In the recusion process this will be the highest index of the subList.
	"""
	def quickSort(self, quickSortList, lowIndex = 0, highIndex = -1):
		if highIndex == -1:
			highIndex = len(quickSortList) - 1
		
		if(lowIndex >= highIndex):
			return quickSortList
		
		# middle index
		# pivotIndex = int((lowIndex + highIndex) / 2)
		
		# random pivot index
		# pivotIndex = random.randrange(lowIndex, highIndex)

		# worst case pivotIndex
		pivotIndex = quickSortList.index(min(quickSortList[lowIndex:highIndex]))
		
		newPivotIndex = self.partition(quickSortList, lowIndex, highIndex, quickSortList[pivotIndex])		
		self.quickSort(quickSortList, lowIndex, newPivotIndex -1)
		self.quickSort(quickSortList, newPivotIndex, highIndex)


	"""
	Method used to quicksort a list using recusion.
	This method swaps two indices to the right subList.
	The items on the left of the pivot index are lower than the pivot.
	The items on the right of the pivot index are higher than the pivot.
	
	Parameters
	----------
	quickSortList : List
		The list you want to quickSort. 

	lowIndex: Integer
		The lowest index of the list.
		In the recusion process this will be the lowest index of the subList.

	highIndex: Integer
		The highest index of the list.
		In the recusion process this will be the highest index of the subList.
	
	pivotValue:
		The value of the selected pivot.
	"""
	def partition(self, quickSortList, lowIndex, highIndex, pivotValue):
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
global minValue
global maxValue
global loopCounter
global recursionCounter
loopCounter = 0
minValue = None
maxValue = None
looping = True

sys.setrecursionlimit(10000)
for i in range(10):
	try:
		recursionCounter = 0
		loopCounter += 1
		random.seed()
		unsortedList = [random.randrange(1, amountOfListElements * 2, 1) for x in range(amountOfListElements)]
		qs = quickSort(unsortedList)

		qs.startSort()

		for i in range(len(qs.quickSortList) - 2):
			if not qs.quickSortList[i] <= qs.quickSortList[i]:
				print("not sorted")

		print(qs.counter)
		if maxValue is None or qs.counter > maxValue:
			maxValue = qs.counter
		elif minValue is None or qs.counter < minValue:
			minValue = qs.counter

		#print(recursionCounter)
	except KeyboardInterrupt:
		break


print("max: ", maxValue)
print("min: ", minValue)
print("amount of tests: ", loopCounter)
		
# middle of list pivot
#	max :  151746
#	min :  90690
#	loop:  6738
