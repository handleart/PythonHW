# Art Mostofi
# Implementing an Unordered List Structure in Python

class Node:
		def __init__(self,initData):
			self.data = initData
			self.next = None

		def getData(self):
			return self.data

		def getNext(self):
			return self.next

		def setData(self, newData):
			self.data = newData

		def setNext(self, newNext):
			self.next = newNext

class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0

		while current != None:
			count += 1;
			current = current.getNext()

		return count

	def search(self, item):
		current = self.head
		found = False

		while current != None and not found :
			if (current.getData() == item):
				found = True
			else:
				current = current.getNext()
		
		return found

	def remove(self, item):
		#find item
		current = self.head
		previous = None
		found = False
		count = 0

		#while current.getData() != item and current.getData() != None:
		while not found and current != None:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

			
			#test case
			#count += 1
			#print count
			#if count > 100:
			#	break

		if found == True:
			if previous == None:
				self.head = current.getNext()
			else:
				previous.setNext(current.getNext())
			
		#print found

A = UnorderedList()
A.add(5)
A.add(23)
A.add(200)
A.add(220)
A.add(0)

#test case middle
A.remove(200)

#test case end
A.remove(5)

#test case begin
A.remove(0)

#test case dpes not exist
A.remove(0)
A.remove(8)