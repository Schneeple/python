import numpy as np


class Node(object):
	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None
		

class BST(object):

	def __init__(self):
		self.root = None
		
	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insertValue(data, self.root)
	
	def insertValue(self,data,node):
		if data < node.data:
			if node.leftChild:
				self.insertValue(data,node.leftChild)
			else:
				node.leftChild = Node(data)
		else:
			if node.rightChild:
				self.insertValue(data,node.rightChild)
			else:
				node.rightChild = Node(data)
	
	def getMinValue(self):
		if self.root:
			return self.GetMin(self.root)
			
	def GetMin(self, node):
		if node.leftChild:
			return self.GetMin(node.leftChild)
		return node.data
		
	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root)
			
	def getMax(self,node):
		if node.rightChild:
			return self.getMax(node.rightChild)
		return node.data
	
	def traverse(self):
		if self.root:
			return self.traverseInorder(self.root)
			
	def traverseInorder(self, node):
		if node.leftChild:
			self.traverseInorder(node.leftChild)
			
		print("%s" % node.data)
		
		if node.rightChild:
			self.traverseInorder(node.rightChild)
			
		
		
bst= BST()

bst.insert(10)
bst.insert(4)
bst.insert(6)
bst.insert(18)
bst.insert(10000)
bst.insert('A')
bst.insert('jsfh')

print bst.traverse() # why does this have a None?

print "MinValue: " + str(bst.getMinValue())
print "MaxValue: " + str(bst.getMaxValue())

			