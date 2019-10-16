class stacknode(object):
	def __init__(self,value, nxt):
		self.value = value
		self.next = nxt

	def __repr__(self):
		nval = self.next and self.next.value or None
		return f"[{self.value} : {repr(nval)}]"

class stack1(object):
	def __init__(self):
		self.top = None

	def push(self, obj):
		node = stacknode(obj, None)
		node.next = self.top
		self.top = node

	def pop(self):
		if self.top is None:
			print("empty stack")
			return None
		node = self.top
		self.top = self.top.next
		return node.value

	def vtop(self):
		if self.top is None:
			print("stack empty")
		return self.top.value

	def count(self):
		if self.top is None:
			return 0
		count = 1
		node = self.top
		while(node.next != None):
			count+=1
			node = node.next
		return count


st = stack1()
st.pop()
print(st.count())
st.push(22)
st.push(12)
print(st.count())
st.vtop()
st.pop()
st.vtop()
st.pop()
print(st.count())
# print(st.top())
st.pop()
# print(st.top())
st.pop()
st.push(23)
print(st.count())