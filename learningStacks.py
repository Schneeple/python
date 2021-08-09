class Stack:
	def __init__(self):
		self.mat = []
	
	def isEmpty(self):
		return self.mat == []
		
	def push(self, data):
		self.mat.append(data)
		
	def pop(self):
		value = self.mat[-1]
		del self.mat[-1]
		return value
		
	def peek(self):
		return self.mat[-1]

	def sizers(self):
		return len(self.mat)


stack = Stack()

stack.push(24)
stack.push(25)
stack.push(28)

print stack.sizers()

print stack.pop()

print stack.peek()




