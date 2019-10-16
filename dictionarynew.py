from dllist import DoubleLinkedList

class Dictionary(object):
	def __init__(self, num_bucket = 256):
		self.map = DoubleLinkedList()
		for i in range(0, num_bucket):
			self.map.push(DoubleLinkedList())

	"""takes a key, convert it to number and get bucket id it will belong to"""
	def hash_key(self, key):
		return hash(key) % self.map.count()

	def get_bucket(self, key):
		bucket_id = self.hash_key(key)
		return self.map.get(bucket_id)

	def get_slot(self, key, default = None):

		"""
		return either a bucket and a node fro the slot , or None, None
		"""
		bucket = self.get_bucket(key)

		if bucket:
			node = bucket.begin
			i=0

			while node:
				if key == node.value[0]:
					return bucket, node
				else :
					node = node.next
					i+=1

		#fall through both if and while above
		return bucket, None

	def get(self, key, default = None):
		bucket, node = self.get_slot(key, default = default)
		return node and node.value[1] or node


	def set(self, key, value):
		bucket, slot = self.get_slot(key)

		if slot:
			slot.value = (key, value)
		else:
			bucket.push((key, value))

	def delete(self, key):
		bucket = self.get_bucket(key)
		node = bucket.begin

		while node:
			k, v = node.value
			if key == k:
				bucket.detach_node(node)
				break

	def list(self):
		bucket_node = self.map.begin
		while bucket_node:
			slot_node = bucket_node.value.begin
			while slot_node:
				print(slot_node.value)
				slot_node = slot_node.next
			bucket_node = bucket_node.next