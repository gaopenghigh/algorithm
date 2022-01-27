# 215. 数组中的第K个最大元素
# 难度中等
# 
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#  
# 提示：
# 
# 1 <= k <= nums.length <= 104
# -104 <= nums[i] <= 104

# 有 4 种主要的算法：
# 1. 暴力，即排序后取第 K 个元素。
# 2. 使用堆，可以构建一个大根堆，然后弹出 k 个元素。
# 3. 如果有一个大小为 K 的集合，里面放当前为止最大的 K 个元素，当发现更大的元素时，就从集合中把最小的一个删掉，然后把新元素放进去。
#    显然这就是一个大小为 K 的小根堆，在构建过程中，如果大小大于 k， 则弹出最小的元素后继续，完成后堆顶元素即是所需答案。
# 4. 借助快速排序的方法。相对于整体全部排序，我们想要的是找到一个位置，排在它左边的都比它小，排在它右边的都比它大。这一点很像快速排序的原理，所以可以稍微调整快速排序的方法，让 pivot 逐渐地靠近倒数第 k 个位置。

from cgitb import small


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        idx = 0
        target = len(nums) - k
        while True:
            idx = self.partition(nums, left, right)
            if idx == target:
                return nums[idx]
            elif idx < target:
                left = idx + 1
            else:
                right = idx - 1

    def partition(self, nums, left, right):
        pivot = nums[left]
        slow = left
        fast = left + 1
        while fast <= right:
            if nums[fast] <= pivot:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1
        nums[slow], nums[left] = nums[left], nums[slow]
        return slow

class SolutionMinHeap:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = MinHeap()
        for i in nums:
            if heap.len() < k or i > heap.top():
                if heap.len() == k:
                    heap.pop()
                heap.add(i)
        return heap.top()

class MinHeap:
    def __init__(self) -> None:
        self.arr = []

    def _sink(self, i):
        length = len(self.arr)
        while i * 2 + 1 < length:
            l = i * 2 + 1
            r = i * 2 + 2
            smallest = i
            if l < length and self.arr[smallest] > self.arr[l]:
                smallest = l
            if r < length and self.arr[smallest] > self.arr[r]:
                smallest = r
            if smallest != i:
                self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]
                i = smallest
            else:
                return
    
    def _swim(self, i):
        root = (i - 1) // 2
        while root >= 0 and self.arr[root] > self.arr[i]:
            self.arr[root], self.arr[i] = self.arr[i], self.arr[root]
            i = root
            root = (i - 1) // 2
    
    def add(self, i):
        self.arr.append(i)
        self._swim(len(self.arr) -1)
    
    def pop(self):
        smallest = self.arr[0]
        length = len(self.arr)
        self.arr[0], self.arr[length - 1] = self.arr[length - 1], self.arr[0]
        self.arr.pop()
        self._sink(0)
        return smallest
    
    def top(self):
        return self.arr[0]

    def len(self):
        return len(self.arr)


if __name__ == '__main__':
    arr = [3,2,1,5,6,4]
    print(SolutionMinHeap().findKthLargest(arr, 2))