import math
import random
import sys 
'''
    Call the buildMaxHeap() function on the list. Also referred to as heapify(), this builds a heap from a list in O(n) operations.
    Swap the first element of the list with the final element. Decrease the considered range of the list by one.
    Call the siftDown() function on the list to sift the new first element to its appropriate index in the heap.
    Go to step (2) unless the considered range of the list is one element.
'''
class MaxHeap():
	def __init__(self, myList):
		self.nodes = list()
		self.sortedList = list()

		for e in myList:
			self.nodes.append(HeapNode(e))
	
	def swap(self, parentLocation, childLocation):
		parentIndex = parentLocation - 1
		childIndex = childLocation - 1
		parent_tmp = self.nodes[parentIndex]
		self.nodes[parentIndex] = self.nodes[childIndex]
		self.nodes[childIndex] = parent_tmp
	
	def __sort(self, childLocation):
		if childLocation > 1:
			
			parentLocation = math.floor(childLocation / 2)
			if self.nodes[childLocation - 1].element > self.nodes[parentLocation - 1].element:
				self.swap(parentLocation, childLocation)

			self.__sort(childLocation - 1)
	
	def pop(self):
		self.__sort(len(self.nodes))
		self.sortedList.append(self.nodes[0])
		self.nodes[0] = self.nodes.pop()

	def heapify(self):
		while len(self.nodes) > 1:
			self.pop()


		self.sortedList.append(self.nodes.pop())
		for x in self.sortedList:
			print(x.element, ' ')

	def print(self):
		for i in range(len(self.nodes)):
			print("i: ", i)
			self.nodes[i].print()



# could be just a value in the list
class HeapNode():
	def __init__(self, e):
		self.element = e

	def print(self):
		print("element:", self.element)

# 9999 max recusion depth how to fix?
# for loop vs recursion
test = 9999
sys.setrecursionlimit(99999)
mx = MaxHeap([random.randint(0, test * test) for i in range(test)])
print("list")
mx.heapify()

