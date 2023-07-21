from stack import Stack


# Text editor undo and redo function	
def textEditor(string, actions):
	stack = Stack()
	history_stack = Stack()
	
	for i in range(len(string)):
		stack.push(string[i])
		
	
	for i in range(len(actions)):
		if actions[i] == 'u':
			value = stack.pop()
			history_stack.push(value)
		else:
			value = history_stack.pop()
			stack.push(value)
	
	print(stack)

textEditor('hello', 'uurruu')
