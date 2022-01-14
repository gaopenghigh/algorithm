import sys
from typing import Annotated
sys.path.append('..')
import lib.util as util

class Node(object):
	def __init__(self, key, val=None, size=1, left=None, right=None) -> None:
		super().__init__()
		self.key = key
		self.val = val
		self.size = size
		self.left = left
		self.right = right
	
	def __str__(self) -> str:
		return "Node(k=%s, v=%s, size=%d" % (self.key, self.val, self.size)

class BST(object):
	def __init__(self) -> None:
		super().__init__()
		self.root = None
	
	def get(self, k):
		node = self.root
		while node is not None:
			if k == node.key:
				return node.val
			elif k < node.key:
				node = node.left
			else:
				node = node.right
		return None
	
	def put(self, k, v):
		self.root = self._put(self.root, k, v)

	def delete(self, k):
		self.root = self._delete(self.root, k)
	
	def size(self):
		return self._size(self.root)
	
	def min_node(self):
		return self._min_node(self.root)

	def delete_min_node(self):
		return self._delete_min_node(self.root)

	@classmethod
	def _put(cls, node, k, v):
		if node is None:
			return Node(k, v)
		if k == node.key:
			node.val = v
		elif k < node.key:
			node.left = cls._put(node.left, k, v)
		else:
			node.right = cls._put(node.right, k, v)
		node.size = cls._size(node.left) + cls._size(node.right) + 1
		return node
	
	@staticmethod
	def _size(node):
		if node is None:
			return 0
		return node.size

	@classmethod
	def _min_node(cls, node):
		if node is None:
			return None
		if node.left is None:
			return node
		return cls._min_node(node.left)
	
	@classmethod
	def _delete_min_node(cls, node):
		if node.left is None:
			return node.right
		node.left = cls._delete_min_node(node.left)
		node.size = cls._size(node.left) + cls._size(node.right) + 1
		return node
	
	# 如果删除的是根节点，由于它的右子树所有节点都比自己大，左子树所有节点都比自己小，所以可以右子树中挑选最小的一个节点来代替自己
	@classmethod
	def _delete(cls, node, k):
		if node is None:
			return None
		if k < node.key:
			node.left = cls._delete(node.left, k)
		elif k > node.key:
			node.right = cls._delete(node.right, k)
		else:
			if node.left is None:
				return node.right
			elif node.right is None:
				return node.left
			else:
				t = node
				node = cls._min_node(t.right)
				node.left = node.left
				node.right = cls._delete_min_node(t.right)
		node.size = cls._size(node.left) + cls._size(node.right) + 1
		return node

	

def test_bst_delete_min():
	arr = [2, 3, 7, 0, 1, 2, 1]
	bst = BST()
	for i in arr:
		bst.put(i, 1000 + i)
	print("--- size", bst.size())
	print('min node is', bst.min_node())

	print('delete k 2')
	bst.delete(2)
	print("--- size", bst.size())
	print('min node is', bst.min_node())

	print(bst.root)

	print('delete k 3')
	bst.delete(3)
	print("--- size", bst.size())
	print('min node is', bst.min_node())

	print('delete k 7')
	bst.delete(7)
	print("--- size", bst.size())
	print('min node is', bst.min_node())

	print('delete k 2')
	bst.delete(2)
	print("--- size", bst.size())
	print('min node is', bst.min_node())

	print('delete k 2 again')
	bst.delete(2)
	print("--- size", bst.size())
	print('min node is', bst.min_node())

	print('delete k 2 again')
	bst.delete(2)
	print("--- size", bst.size())
	print('min node is', bst.min_node())

	print('delete k 1')
	bst.delete(1)
	print("--- size", bst.size())
	print('min node is', bst.min_node())


def test_bst(n):
	arr = util.get_random_array(n)
	util.print_array(arr)
	bst = BST()
	for i in arr:
		bst.put(i, "data-%d" % i)
	print("after put size", bst.size())
	for i in arr:
		bst.delete(i)
		print("after delete %d size" % i, bst.size())
	

if __name__ == '__main__':
	#test_bst_delete_min()
	test_bst(500)