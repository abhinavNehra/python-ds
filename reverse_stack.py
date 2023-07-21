from stack import Stack

class ReverseString(Stack):
	
	def start(self):
		
		result  = ""
		current = self.header
		
		while current != None:
			result += current.data
			current = current.next
		
		return result


print("***********REVERSE*******************")
print("string hello")
reverse = ReverseString()
reverse.push("h")
reverse.push("e")
reverse.push("l")
reverse.push("l")
reverse.push("o")
print('reverse ', reverse.start())
		

