# 47. 全排列 II
# 难度 中等
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 
# 示例 1：
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 
# 示例 2：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# 和 46 题类似，使用标准回溯方法，唯一的变化是可能包含重复数字，而需要返回的是不重复的全排列。

from collections import defaultdict

class Solution:
    def __init__(self) -> None:
        self.res = []
        self.nums = None
        self.used = defaultdict(lambda : False)

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        self.nums = nums
        self.backtrack([])
        return self.res
    
    def backtrack(self, track):
        if len(track) == len(self.nums):
            self.res.append(track[:])
            return
        for i in range(len(self.nums)):
            if self.used[i]:
                continue
            if i >= 1 and self.nums[i] == self.nums[i-1] and not self.used[i-1]:
                continue

            track.append(self.nums[i])
            self.used[i] = True
            self.backtrack(track)
            track.pop()
            self.used[i] = False

