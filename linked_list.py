class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
		
class LinkedList:
	def __init__(self):
		self.header = None
		self.n = 0
		
	def __len__(self):
		return self.n
		
	def __str__(self):
		result = ""
		if self.header is None:
			return result
		current = self.header

		while current is not None:
			result += str(current.data) + "->"
			current = current.next
		return result[:-2]
		
	def insert_head(self, data):
		node = Node(data)
		if self.header == None:
			self.header = node
			self.n += 1
		else:
			node.next = self.header
			self.header = node
			self.n += 1
			
	def insert_tail(self, data):
		node = Node(data)
		
		current = self.header
		while current.next is not None:
			current = current.next
		
		current.next = node
		self.n  += 1
		
	def insert_position(self, data, pos):
		node = Node(data)
		
		count = 1
		current = self.header
		while count < pos :
			current = current.next
			count += 1
		
		node.next = current.next
		current.next = node
		
			
		
ll = LinkedList()
print('empty ll ---', ll)
print('length of empty ll', len(ll))

print('add 3 to head ')
ll.insert_head(3)
print('add 2 to head ')
ll.insert_head(2)
print('add 1 to head ')
ll.insert_head(1)
print('list ---', ll)
print('insert at tail 9')
ll.insert_tail(9)
print('list ----', ll)
print('length ----', len(ll))
print('at 6 at 2 position')
ll.insert_position(6, 2)
print('list---', ll)

