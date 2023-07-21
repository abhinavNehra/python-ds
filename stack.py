# Node for handling data data and next address
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
# Stack class to handle stack functionality	
class Stack:

	# constructor
	def __init__(self):
		self.header = None
		self.length = 0
		
	# Python default function to print class value
	def __str__(self):
		current = self.header
		
		result = ""
		while current is not None:
			result += "->" + str(current.data)
			current = current.next
		
		return result
	
	# Python default function to print class length
	def __len__(self):
		return self.length
	
	# Python function to insert data in stack in LIFO order
	def push(self, data):
		
		# create new node
		new_node = Node(data)
		
		# check for empty header and assign new node to empty header
		if self.header == None:
			self.header = new_node
			self.length += 1
		else:
			temp = self.header
			new_node.next = self.header
			self.header = new_node
			self.length += 1
	
	# In stack we follow LIFO => last in first out policy
	def pop(self):
		node = self.header
		self.header = self.header.next
		self.length -= 1
		return node.data
		
	# Check the top entry
	def peek(self):
		return self.header.data
		
	def is_empty(self):
		if self.header == None:
			return 'Empty'
		else:
			return 'Not Empty'
	
	def size(self):
		return self.length
	
	
		

stack = Stack()
print('stack', len(stack))
print('stack ', stack)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print('stack length', len(stack))
print('print stack---', stack)
print('pop value', stack.pop())
print('print stack---', stack)
print('pop value', stack.pop())
print('print stack---', stack)
print('peek last value entered in stack', stack.peek())
print('stack is empty---', stack.is_empty())
print('stack seize ---', stack.size())
print('pop value', stack.pop())
print('pop value', stack.pop())
print('print stack---', stack)
print('stack is empty---', stack.is_empty())
print('stack seize ---', stack.size())			

			
			
			
			
			
			
			
			
			
