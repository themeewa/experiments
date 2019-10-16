class SingleLinkedListNode(object):
	def __init__(self, value, nxt):
		self.value = value
		self.next = nxt

	def __repr__(self):
		nval = self.next and self.next.value or None
		return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):
	def __init__(self):
		self.begin = None
		self.end = None

	def push(self, obj):
		# append a node at the end of the list
		node = SingleLinkedListNode(obj, None)

		if self.begin == None:
			self.begin = node
			self.end = self.begin
		else:
			self.end.next = node
			self.end = node
			assert self.begin != self.end

		assert self.end.next is None
	def pop(self):
		if self.begin is None:
			return None
		elif self.begin ==self.end:
			node = self.begin
			self.begin = self.end = None
			return node
		else:
			node =self.begin
			while(node.next != self.end):
				node = node.next
			assert self.end != node
			self.end = node
			return node.next.value

	def printlist(self):
		head = self.begin
		while(self.end != head):
			print(head.value)
			head = head.next
		print(head.value)

# def addnode(head,newn):
# 	if head == None:
# 		return newn
# 	if head.next==None:
# 		head.next = newn
# 	else:
# 		_ = addnode(head.next,newn)
# 	return head

# def printlist(head):
# 	if head is not None:
# 		print(head.value)
# 		printlist(head.next)
# 	else:
# 		pass
# def delhead(head):
# 	temp = head
# 	del head
# 	return temp.next

ll = SingleLinkedList()
# print(ll.begin)
ll.push('car0')
# ll.printlist()
ll.push('car1')
ll.push('car2')
ll.push('car3')
ll.push('car1')
ll.push('car2')
ll.push('car3')
ll.printlist()
print(ll.pop())
print(ll.pop())
print(ll.pop())
print(ll.pop())
ll.printlist()