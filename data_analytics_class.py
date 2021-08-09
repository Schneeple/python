import numpy as np

									# Arrays
								#.................

print "Array Section"
numbers = np.linspace(10,15,6)

# O(1) for pulling an index
first_num=numbers[0]
print first_num

# O(N) for adding or deleting an index or scanning through all of the array
numbers[3]=100
largest_value=numbers[0]
for num in numbers:
	if num > largest_value:
		largest_value = num
print largest_value







								# Linked Lists 
							# ....................
print "Linked List Section"


# node1-> node2 -> node3 -> null
# single node can: contain data and reference to next node
# must be a class to point
# can not use indexes to find data!!!
# must iterate though all nodes to find data
# O(1) time complexity
# Much more dynamic data structures than arrays


# DISADVANTAGES
# Use a lot of memory to make multiple classes
# Can not add index to very end


# INSERTION  at the BEGINING an be used for this O(1):
#linkedList.insertAtStart(10)

# INSERTION  at the END an be used for this   O(N):
# linkedList.insertAtEnd(25)

# REMOVE an indexO(N)
# can use an equality by using linkedList.remove(10) to find the value 10


					# Linked List 			# Arrays
#	Search				N						1
#	Insert at start		1						N
# 	Insert at end		N						1
# 	Deletion			N						0


class Node(object):

	def __init__(self,data):
		self.data = data
		self.nextNode = None
		
		
class LinkedList(object):

	def __init__(self):
		self.head = None
		self.size = 0
	
	
	# O(1)
	def insertAtStart(self, data):
		self.size = self.size +1
		newNode = Node(data)
		
		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode
	# O(1)
	def size1(self):   # if head is a null
		return self.size
		
	# O(N)	
	def size2(self):
		actualNode = self.head
		size = 0
		while actualNode is not None:
			size+=1
			actualNode = actualNode.nextNode
	
	# O(N)
	def insertAtEnd(self, data):
		self.size = self.size + 1
		newNode = Node(data)
		actualNode = self.head
		
		while actualNode.nextNode is not None:
			actualNode= actualNode.nextNode
			
		actualNode.nextNode = newNode			



	def traverseList(self):
		actualNode = self.head
		while actualNode != None:
			print '%d' % actualNode.data   # Not sure what that says
			actualNode = actualNode.nextNode


	def removeList(self,data):
	
		if self.head is None:
			return
			
		self.size = self.size - 1
		currentNode = self.head
		previousNode = None
		
		while currentNode.data is not data:
			previousNode = currentNode
			currentNode = currentNode.nextNode
			
		
		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode   	
		
		


# Application of LinkedLists
linkedList = LinkedList()
linkedList.insertAtStart(245)
linkedList.insertAtStart(20)
linkedList.insertAtStart(10)
linkedList.insertAtEnd(40)

print linkedList.size1()

linkedList.removeList(20)
linkedList.removeList(10)
linkedList.removeList(245)


print linkedList.size1()

# Double Linked List video makes should be rewatched if needed
		# O(1) is the node is known and not needed to be searched for




								    # Stacks 
							# ....................
print "Stack and Heap Section"


# Lesson 18
# abstract data type
# basic operations: pop(), push(), peep()
# easily implemented with arrays or linekd lists
# they define basic operations( add two numbers together)
# finding Euler-cycles in a graph
# O(1)
# push() operations add to the stack
# pop() opeartions will REMOVE the last item out of the stack
# peek() operations will RETURN the last item without removing

# Lesson 19
# call stack is abstract data type taht stores information about the 
	#subroutines/ methods/ and functions of a program
# Stores temporary variables (e.g. 2+2 = 4, the 2 and 2 will be freed)
# stack memory uses RAM which is limited

# Heap is a region of memory that is not managed automatically for you
# is memory is not taken off the heap it is a "memory leak"



# stacked memory				|	heap memory
# limited in size				|	no size limits
# fast access					|	slow access
# local variables				|	objects
# space is managed by CPU		|	memory may be fragmented
# variables cannot be resized	|	variables can be resized



# Lesson 20
# Stack and Recursion 
# Recursive methods are helpful for: DFS, traversing a binary tree, looking for an item in linekd list
# NEED BASE CASE to avoid stack overflow
# the factorial is a common recursive method
# not usable for the factorial of 1 million, it will get a stack overflow

# Lesson 21
# Implement Stacks using arrays
# LIFO structure

class Stack:

	def __init__(self):
		self.stack = []
		
	def isEmpty(self):
		return self.stack == []
		
	def push(self,data):	
		self.stack.append(data)
		
	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data 		# important to get data
		
	def peep(self):
		return self.stack[-1]
		
		
	def sizeStack(self):
		return len(self.stack)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print stack.sizeStack()
print "Popped:" , stack.pop()
print "Popped:" , stack.pop()
print stack.sizeStack()
print " Peeped:" , stack.peep()
print stack.sizeStack()




		


