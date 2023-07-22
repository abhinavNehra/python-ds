
from stack import Stack

class find_celebirity(Stack):
	
	def __init__(self):
		self.relation = [
					[0,0,1,1],
					[0,0,1,1],
					[0,0,0,0],
					[0,0,1,0]
				]
		# store all the celebiraty
		self.stack = Stack()
		for i in range(len(self.relation)):
			self.stack.push(i)
				
	def find(self):
		while(len(self.stack) != 0):
			c1 = self.stack.pop()
			c2 = self.stack.pop()
			print(f'[{c1}][{c2}]---',self.relation[c1][c2] )
			print(f'[{c2}][{c1}]---',self.relation[c2][c1] )

			if self.relation[c1][c2]:
				self.stack.push(c2)
			elif self.relation[c2][c1]:
				self.stack.push(c1)
			
			if (len(self.stack) == 1):
				break
				
		print('fc ===', self.stack)
		celeb = self.stack.pop()
		
		for i in range(len(self.relation)):
			
			if i != celeb:
				if self.relation[i][celeb] == 0 or self.relation[celeb][i] == 1:
					print("No one is celeb")
					return
		
		print(f"celeb is at {celeb + 1} position") 
	
fc = find_celebirity()
fc.find()	
		
		
		
