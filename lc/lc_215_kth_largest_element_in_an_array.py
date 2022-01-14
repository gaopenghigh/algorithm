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
# 2. 使用堆，可以构建一个大根堆，然后弹出 k 个元素。还可以构建一个大小为 K 的小根堆，在构建过程中，如果大小大于 k， 则弹出最小的元素后继续，完成后堆顶元素即是所需答案。
# 3. 借助快速排序的方法。相对于整体全部排序，我们想要的是找到一个位置，排在它左边的都比它小，排在它右边的都比它大。这一点很像快速排序的原理，所以可以稍微调整快速排序的方法，让 pivot 逐渐地靠近倒数第 k 个位置。

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

class SolutionMaxHeap:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq = PQ()
        for i in nums:
            pq.add(i)
        ret = None
        for i in range(k):
            ret = pq.pop()
        return ret

class PQ(object):
    def __init__(self) -> None:
        super().__init__()
        self.arr = []
        self.length = 0

    def _sink(self, i):
        while i * 2 + 1 < self.length:
            l = i * 2 + 1
            r = i * 2 + 2
            largest = i
            if l < self.length and self.arr[largest] < self.arr[l]:
                largest = l
            if r < self.length and self.arr[largest] < self.arr[r]:
                largest = r
            if largest != i:
                self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
                i = largest
            else:
                return
    
    def _swim(self, i):
        root = (i - 1) // 2
        while root >= 0 and self.arr[root] < self.arr[i]:
            self.arr[root], self.arr[i] = self.arr[i], self.arr[root]
            i = root
            root = (i - 1) // 2
    
    def add(self, i):
        self.arr.append(i)
        self.length += 1
        self._swim(self.length -1)
    
    def pop(self):
        larget = self.arr[0]
        self.arr[0], self.arr[self.length - 1] = self.arr[self.length - 1], self.arr[0]
        self.length -= 1
        self._sink(0)
        return larget


if __name__ == '__main__':
    arr = [3,2,1,5,6,4]
    print(Solution().findKthLargest(arr, 2))