# Frits Dannenberg Nov 17 2018 
# Utrecht University of Applied Sciences

# Implements heapsort. 
# Accepts any iterable object containing comparable elements, and hence the solution is not in-place.
# Heapsort is not stable.
# Also see https://en.wikipedia.org/wiki/Heapsort#/media/File:Heapsort-example.gif

# Indices of the array correspond to positions in the binary tree  
# by enumerating top-to-bottom, left-to-right.

import math


class maxheap():

	def __init__(self,myList):

		self.array = [None] * len(myList)
		self.size = 0

		for e in myList:
			self.insert(e)

	def insert(self,e):
	
		self.array[self.size] = e
		self.checkbottominsert(self.size)

		self.size = self.size + 1
	
	def swap(self, a, b):
		
		temp = self.array[b]
		self.array[b] = self.array[a]
		self.array[a] = temp
	
	# swap the child with the parent to maintain the heap property
	# n is a legal position in the heap. 
	def checkbottominsert(self, n):
		
		if n < 1:
			return

		parent = math.floor( (n-1) / 2 )		

		if self.array[parent] < self.array[n]:
			
			self.swap(parent, n)
			self.checkbottominsert(parent)


	# swap the parent with the largest child			
	def checktopinsert(self, n = 0):
		
		lchild = 2 * n + 1
		rchild = 2 * n + 2

		# both left and right child do not exist
		if (self.size-1) < lchild:		
			return
		
		# left child exists
		elif (self.size-1) == lchild:		

			# No further checks, element originally at n is now in bottom layer
			if self.array[lchild] > self.array[n]:
				self.swap(lchild, n)

		
		# both left and right child exist
		else:					
			largest = rchild
			if self.array[lchild] > self.array[rchild]:
				largest = lchild

			if self.array[largest] > self.array[n]:
				self.swap(largest, n)
				self.checktopinsert(largest)
			
	def pop(self):
		
		if self.size < 1:
			return None
		
		output = self.array[0]
		self.array[0] = self.array[self.size-1]
		self.size = self.size - 1

		self.checktopinsert()

		return output

x = maxheap([4,5,6,43,3,24,6,67,2342,4,6,-17,23,11])

while x.size > 0:
	print(x.pop())
