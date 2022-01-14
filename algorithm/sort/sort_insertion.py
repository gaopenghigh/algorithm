import sys
sys.path.append('..')
import lib.util_sort as lib

@lib.print_spend_time
def sort_insertion_array(arr):
	i = 0
	while i < len(arr):
		j = i
		while j > 0 and arr[j] < arr[j-1]:
			arr[j], arr[j-1] = arr[j-1], arr[j]
			j = j - 1
		i = i + 1
	return arr

@lib.print_spend_time
def sort_insertion_list(head):
	sorted = None
	curr = head
	while curr is not None:
		next = curr.next
		sorted = _insert_one(sorted, curr)
		curr = next
	head = sorted
	return head

def _insert_one(head, node):
	if head is None or head.val > node.val:
		node.next = head
		head = node
	else:
		curr = head
		i = 0
		while curr.next is not None and curr.next.val < node.val:
			i += 1
			curr = curr.next
		node.next = curr.next
		curr.next = node
	return head


def test_sort_insertion(n):
	node_list = lib.get_random_node_list(n)
	sort_insertion_list(node_list)

	arr = lib.get_random_array(n)
	sort_insertion_array(arr)

if __name__ == '__main__':
	test_sort_insertion(10000)
