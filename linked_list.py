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
		
	def __getitem__(self, index):
		current = self.header
		pos = 1
		while pos < index:
			current = current.next
			pos += 1
			
		return current.data
		
	def __delitem__(self, index):
		current = self.header
		pos = 1
		while pos < index:
			current = current.next
			pos += 1
		
		current.next = current.next.next
			
		
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
		
		if self.n == 0:
			self.header = node
			self.n += 1
			return 
		current = self.header
		while current.next is not None:
			current = current.next
		
		current.next = node
		self.n  += 1
		
	def insert_position(self, data, pos):
		node = Node(data)
		if pos > self.n - 1:
			return 'Wrong Idex Given'
			
		count = 0
		current = self.header
		while count < pos :
			current = current.next
			count += 1
		
		node.next = current.next
		current.next = node
		self.n += 1
		
	def clear(self):
		self.header = None
		self.n = 0
	
	def delete_from_head(self):
		self.header = self.header.next
		self.n -= 1
	
	def delete_from_tail(self):
		current = self.header
		while current.next.next is not None:
			current = current.next
		current.next = None
		self.n -= 1
	
	def delete_by_value(self, value):
		current = self.header
		while current is not None:
			if current.next.data == value:
				break
			current = current.next
		
		current.next = current.next.next
		self.n - 1
				

	def find_data(self, data):
		current = self.header
		pos = 0
		while current is not None:
			if current.data == data:
				break
			pos += 1
			current = current.next
		
		return pos
		
	def reverse_list(self):
		current = self.header
		temp = current.next
		current.next = None

		while temp is not None:
			
			temp_next = temp.next
			temp.next = current
			current = temp
			temp = temp_next
			self.header = current

		
		self.header = current
		
		
	def fomat_sentence(self):
		
		# replace * an / with single space
		# two consicutive * or / replace those consicutive with single space
		# and convert next character to upper case
		
		current  = self.header

		while current is not None:
			if current.data == '*' and current.next.data == '*' or current.data == '/' and current.next.data == '/' or current.data == '/' and current.next.data == '*' or current.data == '*' and current.next.data == '/' :
				current.data = " "
				current.next.data = ""
				current.next.next.data = current.next.next.data.upper()
			elif current.data == '*' or current.data == '/':
				current.data = " "
			
			current = current.next
		
		

		
		
			
		
			
		
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
print('reverse')
ll.reverse_list()
print(ll)
print('length ----', len(ll))
print('list---', ll)
print('insert 6 at 2nd position')
ll.insert_position(6, 2)
print('list---', ll)

print('search  postion 6 from list')
print(ll.find_data(6))

print('get value at ll[2]', ll[2])
print('get value at ll[3]', ll[3])

print('delete first node from list')
ll.delete_from_head()
print(ll)
print('delete last node from list')
ll.delete_from_tail()
print(ll)
print('delete  value 6 from list')
ll.delete_by_value(6)
print(ll)


print('clearing list')
ll.clear()
print('length of list', len(ll))




character_ll = LinkedList()
character_ll.insert_tail("T")
character_ll.insert_tail("h")
character_ll.insert_tail("e")
character_ll.insert_tail("/")
character_ll.insert_tail("*")
character_ll.insert_tail("s")
character_ll.insert_tail("k")
character_ll.insert_tail("y")
character_ll.insert_tail("*")
character_ll.insert_tail("i")
character_ll.insert_tail("s")
character_ll.insert_tail("/")
character_ll.insert_tail("/")
character_ll.insert_tail("b")
character_ll.insert_tail("l")
character_ll.insert_tail("u")
character_ll.insert_tail("e")
print(character_ll)
character_ll.fomat_sentence()
print(character_ll)


