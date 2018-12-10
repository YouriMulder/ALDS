# Studentnumber : 1716390
# Class : V2C

class ListNode:
	"""
	Constructor of the ListNode class.
	
	Parameters
	----------
	data : unknown
		The data you want to store the node.

	nextNode : ListNode
		The next node in the linked list.
	"""
	def __init__(self,data,next_node):
		self.data = data
		self.next = next_node

	"""
	Method to print the data of a node.
	
	Returns
	-------
	str
		string containing the value stored in data
	"""
	def __repr__(self):
		return str(self.data)

class MyCirculairLinkedList:
	
	"""
	Constructor of the myCirculairLinkedList class.
	Head is the start of the linked list.
	Tail is the end of the linked List.
	"""

	def __init__(self):
		self.head = None
		self.tail = None
	
	"""
	Method to print the data of all the nodes in the linked list.
	
	Returns
	-------
	str
		string containing the values of all the nodes in the linked list.
	"""
	def __repr__(self):
		s = ''
		current = self.head
		if current != None:
			s = s + str(current)
			current = current.next
		while current != None and current != self.head:
			s = s + " -> " + str(current)
			current = current.next
		if not s: # s == '':
			s = 'empty list'
		return s

	"""
	Method to check whether the given position i is possible.
	This should be a positions where the queen can't be attacked by others.

	Parameters
	----------
	e : unknown (Didn't choose the name myself. Was given in the reader)
		The value you want to store in the node you are adding to the linked list.
	"""
	def addLast(self,e):
		if not self.head: # self.head == None:
			self.head = ListNode(e,None)
			self.tail = self.head

			# make circulair
			self.tail.next = self.head

		else:
			n = ListNode(e,self.head)
			self.tail.next = n
			self.tail = self.tail.next

	
	"""
	Method to delete a node by value.
	The first item containing this value will be deleted.

	Parameters
	----------
	e : unknown (Didn't choose the name myself. Was given in the reader)
		The value you want to from linked list.
	"""
	def delete(self,e):
		if self.head: # self.head != None:		
			if self.head.data == e:
				
				if self.head is self.tail:
					self.head = None		
				else:
					self.head = self.head.next
				
				if self.head == None:
					self.tail = None
				else:
					self.tail.next = self.head			
			else:
				current = self.head
				while current.next != None and current.next.data != e and current.next != self.head:
		
					current = current.next

				if current.next != None:
					current.next = current.next.next
				if current.next == None:
					self.tail = current
					self.tail.next = self.head


if __name__ == '__main__':
	mylist =  MyCirculairLinkedList()

	# test case according to feedback.
	mylist.delete(2)
	mylist.addLast(1)
	print("Test")
	mylist.delete(2)

	mylist =  MyCirculairLinkedList()
	print(mylist)
	mylist.addLast(1)
	mylist.addLast(2)
	mylist.addLast(3)
	print(mylist)
	mylist.delete(2)
	print(mylist)
	mylist.delete(1)
	print(mylist)
	mylist.delete(3)
	print(mylist)

	mylist.addLast(1)
	mylist.addLast(2)
	mylist.addLast(3)
	print(mylist)
	
	mylist.delete(1)
	print(mylist)
	print(mylist.tail.next == mylist.head)
	
	mylist.addLast(5)
	print(mylist)
	print(mylist.tail.next == mylist.head)
	
	mylist.delete(2)
	print(mylist)
	print(mylist.tail.next == mylist.head)
	
	mylist.delete(3)
	print(mylist)
	print(mylist.tail.next == mylist.head)
	
	mylist.delete(mylist.tail.data)
	print(mylist.head == None)
	print(mylist.tail == None)
	print(mylist)