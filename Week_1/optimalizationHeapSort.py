import random
import sys 

import time
'''
    Call the buildMaxHeap() function on the list. Also referred to as heapify(), this builds a heap from a list in O(n) operations.
    Swap the first element of the list with the final element. Decrease the considered range of the list by one.
    Call the siftDown() function on the list to sift the new first element to its appropriate index in the heap.
    Go to step (2) unless the considered range of the list is one element.
'''
class MaxHeap():
	def __init__(self, myList):
		# insert not sorted
		self.nodes = myList
		self.sortedList = list()
	
	def swap(self, parentLocation, childLocation):
		parentIndex = parentLocation - 1
		childIndex = childLocation - 1
		parent_tmp = self.nodes[parentIndex]
		self.nodes[parentIndex] = self.nodes[childIndex]
		self.nodes[childIndex] = parent_tmp
	
	def __sort(self, childLocation):
		while childLocation > 1:
		#if childLocation > 1:
			parentLocation = int(childLocation / 2)
			if self.nodes[childLocation - 1] > self.nodes[parentLocation - 1]:
				self.swap(parentLocation, childLocation)

			#self.__sort(childLocation-1)
			childLocation -= 1
	
	def pop(self):
		self.__sort(len(self.nodes))
		self.sortedList.append(self.nodes[0])
		self.nodes[0] = self.nodes.pop()

	def heapify(self):
		while len(self.nodes) > 1:
			self.pop()

		self.sortedList.append(self.nodes.pop())
		return self.sortedList

	def print(self):
		for i in range(len(self.nodes)):
			print("i: ", i)
			print(self.nodes[i])

# 9999 max recusion depth how to fix?
# for loop vs recursion
for i in range(4):
	test = 10 * 10
	sys.setrecursionlimit(99999)
	mx = MaxHeap([random.randint(0, test * test) for i in range(test)])

	print("list")
	start = time.time()
	sortedList = mx.heapify()
	end = time.time()
	print("time", end - start)

	print(sortedList)

#for x in sortedList:
#	print(x)


# while loop seconds 10'000
#time 21.456766366958618
#time 21.50308847427368
#time 22.237149953842163
#time 22.231287240982056

# recusie seconds 10'000
#time 34.25174427032471
#time 34.42176842689514
#time 33.68296027183533
#time 33.88200664520264
