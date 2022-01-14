import sys
sys.path.append('..')
import lib.util_sort as lib

def heapify_max(arr, n, i):
	l = 2 * i + 1
	r = 2 * i + 2
	largest = i
	if l < n and arr[l] > arr[largest]:
		largest = l
	if r < n and arr[r] > arr[largest]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify_max(arr, n, largest)

def build_max_heap(arr):
	n = len(arr)
	for i in range(n//2 - 1, -1, -1):
		heapify_max(arr, n, i)

def sort_heap(arr):
	n = len(arr)
	build_max_heap(arr)
	for i in range(n - 1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify_max(arr, i, 0)

@lib.print_spend_time
def test_sort_heap(n):
	arr = lib.get_random_array(n)
	sort_heap(arr)

if __name__ == '__main__':
	test_sort_heap(800000)