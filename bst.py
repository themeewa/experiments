class BSTreeNode(object):
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

class BSTree(object):
	def __init__(self, rootval,left, right):
		self.root = BSTreeNode( rootval, left, right)

	def get(self, value):
		pass

	def set(self, value):
		parent = node = self.root

		while node:
			if node.value<value:
				parent = node
				node = node.left
			else:
				parent = node
				node = node.right

		if parent.value<value:
			parent.left = BSTreeNode(value, None, None)

		else:
			parent.right = BSTreeNode(value, None, None)

	def printtree(self, node):
		if node:
			print(node.value)
			print("[ left: {}, right: {} ]".format(self.printtree( node.left),self.printtree( node.right)))
			print('*'*10)
			# if node.left:
			# 	self.printtree( node.left)
			# if node.right:
			# 	self.printtree( node.right)

	def pr(self):
		print(self.root.value,self.root.left.value)

newtree = BSTree( 12, None, None)
newtree.set(22)
newtree.printtree(newtree.root)
newtree.pr()