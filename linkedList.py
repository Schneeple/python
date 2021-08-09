class Node(object):
	def __init__(self, data):
		self.data = data
		self.nextNode = None
		
class LL(object):
	def __init__(self):
		self.size = 0
		self.head = None
		
	def Start(self, data):
		self.size += 1
		newNode = Node(data)
		
		if not self.head:
			self.head = newNode
		else:
			newNode.NextNode = self.head
			self.head = newNode
			
		
		
	def End(self, data):
		self.size +=1
		newNode = Node(data)
		actualNode = self.head
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode
			
		actualNode.nextNode = newNode
		newNode.nextNode = None
		
		
	def removers(self, data):
	
		if self.head is None:
			return
	
		self.size = self.size - 1
		currentNode= self.head
		previousNode = None
		
		while currentNode.data is not data:
			previousNode = currentNode
			currentNode= currentNode.nextNode 
			
			
		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode
		
		
		
	def sizeMatters(self):
		return self.size
		
			
		
linkedlist = LL()
print "new"
linkedlist.Start(10)
print linkedlist.sizeMatters()

linkedlist.Start(20)
linkedlist.End(2000)
print linkedlist.sizeMatters()

linkedlist.removers(20)
print linkedlist.sizeMatters()

linkedlist.removers(2000)
print linkedlist.sizeMatters()






