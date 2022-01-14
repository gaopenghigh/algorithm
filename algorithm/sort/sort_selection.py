import sys
sys.path.append('..')
import lib.util_sort as lib

# 原理就是找到剩下列表中最小的一个元素出来放在最前面，如此这般
# O(n^2)
@lib.print_spend_time
def sort_selection_arr(arr):
	i = 0
	while i < len(arr):
		j = i + 1
		while j < len(arr):
			if arr[j] < arr[i]:
				arr[i], arr[j] = arr[j], arr[i]
			j = j + 1
		i = i + 1

@lib.print_spend_time
def sort_selection_list(head_ref):
	sorted_list_tail = None
	curr = head_ref
	while curr is not None:
		curr, min_node = pick_min_node(curr)
		if sorted_list_tail is None:
			head_ref = min_node
		else:
			sorted_list_tail.next = min_node
		sorted_list_tail = min_node
	return head_ref

def pick_min_node(head_ref):
	min_node = None
	min_node_pre = None
	curr = head_ref
	curr_pre = None
	while curr is not None:
		if min_node is None or curr.val < min_node.val:
			min_node_pre = curr_pre
			min_node = curr
		curr_pre = curr
		curr = curr.next
	if min_node_pre is None:
		head_ref = min_node.next
	else:
		min_node_pre.next = min_node.next
	min_node.next = None
	return head_ref, min_node
	

def test_sort_selection(n):
	arr = lib.get_random_array(n)
	sort_selection_arr(arr)

	node_list = lib.get_random_node_list(n)
	sort_selection_list(node_list)

if __name__ == '__main__':
	test_sort_selection(100)