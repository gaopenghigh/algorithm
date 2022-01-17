# 239. 滑动窗口最大值
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口中的最大值。

# 使用单调队列。所谓单调队列，首先是一个 FIFO 的队列，在此基础上，新加入的元素会把它之前所有比它小（大）的元素压扁，这样队列头部的元素一定是当前队列中最大的。

class MonotonicQueue:
    def __init__(self) -> None:
        self.data = []
    def max(self):
        if self.data:
            return self.data[0]
    # 如果队首是 v 就把它删除，否则 v 可能已经被压扁掉了
    def remove(self, v):
        if self.data and self.data[0] == v:
            self.data.pop(0)
    def add(self, v):
        while self.data and self.data[-1] < v:
            self.data.pop()
        self.data.append(v)

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = MonotonicQueue()
        for i in range(k - 1):
            q.add(nums[i])
        i = k - 1
        while i < len(nums):
            q.add(nums[i])
            res.append(q.max())
            q.remove(nums[i+1-k])
            i += 1
        return res

if __name__ == '__main__':
    nums = [1,3,1,4,2,3,7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))