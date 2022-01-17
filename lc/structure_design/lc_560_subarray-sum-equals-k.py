# 560. 和为 K 的子数组
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

# 前缀和的思想，加上一点优化，注意题目只需要求解个数，而非具体哪些子数组，所以我们可以从左到右遍历数组，计算前缀和，
# 同时使用一个 map 记录遍历到当前元素时，该前缀和出息的次数，也就是在当前元素左边数组中，前缀和与当前前缀和一样的子数组的个数

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        pre_sum_count = defaultdict(lambda: 0)
        pre_sum_count[0] = 1 # base case of empty sub string
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum = pre_sum + nums[i]
            pre_sum_need = pre_sum - k
            if pre_sum_need in pre_sum_count:
                res += pre_sum_count[pre_sum_need]
            pre_sum_count[pre_sum] += 1
        return res