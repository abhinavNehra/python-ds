import ctypes

class MeraList:
	
	# constructor
	def __init__(self):
		self.size = 1
		self.n = 0
		self.A = self.__make_array(self.size)
		
	# python function to print some string instead of class object
	def __str__(self):
		result = ""

		for i in range(0, self.n):
			result += str(self.A[i]) + ","
		
		return "[" + result[:-1] + "]"
		
	# python function to enable use of python 'len' function
	def __len__(self):
		return self.n
		
	# python function to get the value of index passed like 'L[2]'
	def __getitem__(self, index):
		if  index > self.n:
			return "Index out of bound"
		
		return self.A[index]
	
	# python function to delte the value of given index like del L[2]
	def __delitem__(self, index):
		if 0 > index > self.n:
			return 'Invalid index'
		
		for i in range(index, self.n - 1):
			self.A[i] = self.A[i + 1]
			
		self.n -= 1
	
	
	#created c type list on initilization
	def __make_array(self, capacity):
		return (capacity*ctypes.py_object)()
		
		
	def append(self, data):
		if self.n >= self.size:
			self.__resize(self.size * 2)
		
		self.A[self.n] = data
		self.n +=1

		
	def __resize(self, size):
		B = self.__make_array(size)
		for i in range(0, self.n):
			B[i] = self.A[i]
		
		self.A = B
		self.size = size
	
	def find(self, value):
		position = None
		for i in range(0, self.n):
			if value == self.A[i]:
				position = i
				break;
		
		if position is not None:
			return position
		else:
			return "Value not found"
			
	def insert(self, value, pos):
		if pos > self.n:
			return "Not a correct position"
			
		if self.n == self.size:
			self.__resize(self.size *2)
		for i in range(self.n, pos, -1):
				self.A[i] = self.A[i-1]
			
		self.A[pos] = value
		self.n += 1
		
	

			
	def pop(self):
		value = self.A[self.n - 1]
		self.n -= 1
		return value
		
	def clear(self):
		self.size = 1
		self.n = 0
		self.A = self.__make_array(self.size)
		
	def findHigestPosition(self, array, length):
		largest = 0
		for i in range(1, length):
			print(array[i])
			if array [i] > array[largest]:
				largest = i
		return largest
		
	def sort(self):
		B = self.__make_array(self.size)
		
		for i in range(0, self.n):
			B[i] = self.A[i]
		
		for i in range(0, self.n):
			pos = self.findHigestPosition(B, self.n - i)
			index = self.n - 1 - i
			temp = B[index]
			B[index] = B[pos]
			B[pos] = temp
		
		self.A = B
		
	def max(self):
		pos = self.findHigestPosition(self.A, self.n)
		return self.A[pos]
		
	def min(self):
		small = self.A[0]
		for i in range(1, self.n):
			if self.A[i] < self.A[small]:
				small = self.A[i]
		return small
		
	def sum(self):
		sum = 0
		for i in range(1, self.n):
			sum += self.A[i]
		return sum
			
				
		
		
		


L = MeraList()
print(L)
print(len(L))
L.append(12)
L.append(21)
L.append(1)
L.append(9)


print(len(L))
print(L)


print(' value at L[2]', L[2])
print('value at L[3]', L[3])
print("find index of value 1 => ", L.find(1))
print(len(L))
print("inert value 23 at 3 position", L.insert(23,2))
print("print array", L)
print("inert value 63 at 0 position", L.insert(63,0))
print("print array", L)
del L[2]
print("print array", L)
print("sort ", L.sort())
print("print array", L)
print("print array largest number", L.max())
print("print array smallest number", L.min())
print("print array sum of array vlaues", L.sum())
print('pop', L.pop())
print('clear the array', L.clear())
print('length of array ', len(L))

	
