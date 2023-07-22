from stack import Stack

def balanced_parantheses(string):
	
	stack = Stack()
	for i in range(len(string)):

		if "({[".find(string[i]) != -1:
			stack.push(string[i])
		elif ")}]".find(string[i]) != -1:
			if len(stack) <= 0:
				print("Not a balanced parantheses")
				return
				
			peek = stack.peek()
			print("string", string[i])
			print("peek", peek)
			if string[i] == ")" and peek == "(" or string[i] == "}" and peek == "{" or string[i] == "]" and peek == "[":
				stack.pop()
			else:
				print("Not a balanced paranthese")
				return 
		
	
	print("balanced parantheses")
		

balanced_parantheses("[{(a + b) + (a + b)}]")
balanced_parantheses("[{(a + b) + (a + b)]]")
balanced_parantheses("[{(a + b) + (a + b)}]}")
