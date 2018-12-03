class ListNode:
	def __init__(self,data,next_node):
		self.data = data
		self.next = next_node

	def __repr__(self):
		return str(self.data)

class MyCirculairLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

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
				while current.next != None and current.next.data != e:
					current = current.next
				if current.next != None:
					current.next = current.next.next
				if current.next == None:
					self.tail = current
					self.tail.next = self.head


if __name__ == '__main__':
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

	