# 300. 最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#  
# 示例 1：
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 
# 示例 2：
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 
# 示例 3：
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1

# 动态规划问题。
# dp[i] 表示以 i 结尾的最长严格递增子序列的长度，显然 dp[0] = 1，dp[i] 最小值为 1
# d[i] 的计算方式为：
# d[i] = max([dp[j] + 1 for j in range(0, i) if nums[j] < nums[i]])

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max([dp[i], dp[j] + 1])
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    nums = [7,7,7,7,7,7,7]
    print(s.lengthOfLIS(nums))