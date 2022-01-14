import sys
sys.path.append('..')
import lib.util_sort as lib

def sort_merge_array(arr):
	if len(arr) == 1:
		return arr
	mid = int(len(arr) / 2)
	left = sort_merge_array(arr[:mid])
	right = sort_merge_array(arr[mid:])
	merged = _merge_array(left, right)
	return merged

def _merge_array(a, b):
	i, j = 0, 0
	merged = []
	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			merged.append(a[i])
			i = i + 1
		else:
			merged.append(b[j])
			j = j + 1
	merged = merged + a[i:]
	merged = merged + b[j:]
	return merged


def sort_merge_list(head_ref):
	length = len(head_ref)
	if length == 1:
		return head_ref

	i = 0
	left = head_ref
	curr = head_ref
	while i < int(length / 2 - 1):
		curr = curr.next
		i += 1
	right = curr.next
	curr.next = None

	sorted_left = sort_merge_list(left) 
	sorted_right = sort_merge_list(right) 
	return _merge_list(sorted_left, sorted_right)


def _merge_list(a, b):
	i, j = a, b
	merged = None
	merged_tail = None
	while i is not None and j is not None:
		min_node = None
		if i.val <= j.val:
			min_node = i
			i = i.next
		else:
			min_node = j
			j = j.next
		min_node.next = None
		if merged_tail is None:
			merged_tail = min_node
			merged = merged_tail
		else:
			merged_tail.next = min_node
			merged_tail = min_node
	if i is not None:
		merged_tail.next = i
	if j is not None:
		merged_tail.next = j
	return merged


@lib.print_spend_time
def test_sort_merge_array(n):
	arr = lib.get_random_array(n)
	sorted_arr = sort_merge_array(arr)

@lib.print_spend_time
def test_sort_merge_list(n):
	node_list = lib.get_random_node_list(n)
	sorted_list = sort_merge_list(node_list)

def _test_merge_list():
	a = lib.Node(1)
	a.next = lib.Node(4)
	a.next.next = lib.Node(7)
	b = lib.Node(2)
	b.next = lib.Node(3)
	b.next.next = lib.Node(8)
	b.next.next.next = lib.Node(8)
	b.next.next.next.next = lib.Node(9)
	lib.print_node_list(_merge_list(a, b))

if __name__ == '__main__':
	test_sort_merge_array(100001)
	test_sort_merge_list(100001)