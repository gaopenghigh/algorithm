import random
import time

class Node(object):
	def __init__(self, val, next=None) -> None:
		super().__init__()
		self.val = val
		self.next = next

	def __str__(self) -> str:
		return "%d" % self.val

	def __len__(self):
		c = 1
		next = self.next
		while next is not None:
			c = c + 1
			next = next.next
		return c

class NodeList(object):
	def __init__(self, head) -> None:
		super().__init__()
		self.head = head

def get_random_array(n=100):
	ret = []
	for _ in range(n):
		ret.append(random.randint(0, n*2))
	return ret

def get_random_node_list(n=100):
	head_ref = Node(random.randint(0, n*2))
	curr = head_ref
	for _ in range(n-1):
		curr.next = Node(random.randint(0, n*2))
		curr = curr.next
	return head_ref

def print_node_list(l):
	p = l
	while p is not None:
		print(p.val, end=" ")
		p = p.next
	print("")

def print_array(arr):
	for i in arr:
		print(i, end=" ")
	print("")

def print_spend_time(f):
	def wrapper(*args, **kwargs):
		start = time.time()
		ret = f(*args, **kwargs)
		end = time.time()
		print("func", f.__name__, "cost time:", (end - start))
		return ret
	return wrapper
