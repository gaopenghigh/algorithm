import sys
sys.path.append('..')
import lib.util_sort as lib

# 通过一个类比容易理解。两个球员，一个前锋，一个守门员，开始时前锋和守门员处于起始位置，路上都是大大小小的球。
# 就以第一个球为 pivot，前锋和守门员从第二个球（位置 1 的球）开始，前锋一步一步往前走，遇到比 pivot 小的球，就让守门员上前一步，然后前锋把当前的球和守门员脚下的球交换，
# 这样，守门员脚下以及身后的球，一定是 <= pivot 的，当然第一个球就是 pivot。
# 当前锋走完全程后，最后把守门员脚下的球和第一个球互换，这样守门员脚下就是 pivot，身后就是 <= pivot 的球，前面则是 > pivot 的球。
def partition_array(arr, low, high):
	pivot = arr[low]
	if low >= high:
		return pivot
	#print('pivot is', pivot, "low is", low, "high is", high)
	# 取 low 为 pivot，small_elements_gate_index 位置以及之前的位置，上面的元素一定 <= pivot
	small_elements_gate_index = low
	i = low + 1
	while i <= high:
		if arr[i] < pivot:
			small_elements_gate_index += 1
			arr[small_elements_gate_index], arr[i] = arr[i], arr[small_elements_gate_index]
		i += 1
	arr[low], arr[small_elements_gate_index] = arr[small_elements_gate_index], arr[low]
	return small_elements_gate_index

def _sort_quick_array(arr, low, high):
	if low < high:
		index = partition_array(arr, low, high)
		_sort_quick_array(arr, low, index-1)
		_sort_quick_array(arr, index+1, high)

def sort_quick_array(arr):
	return _sort_quick_array(arr, 0, len(arr)-1)

@lib.print_spend_time
def test_sort_quick_array(n):
	arr = lib.get_random_array(n)
	sort_quick_array(arr)

if __name__ == '__main__':
	test_sort_quick_array(800000)
