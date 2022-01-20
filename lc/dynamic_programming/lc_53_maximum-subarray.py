# 53. 最大子数组和
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组 是数组中的一个连续部分。
# 
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 
# 示例 2：
# 输入：nums = [1]
# 输出：1
# 
# 示例 3：
# 
# 输入：nums = [5,4,-1,7,8]
# 输出：23
# 
# 提示：
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# 动态规划
# dp(i) 表示以索引 i 结尾的最大和的连续子数组的和
# 如果知道 dp(i-1) 的值，则
#     当 dp[i-1] > 0 时，dp(i) = dp(i-1) + nums[i]
#     否则 dp(i) = nums[i]，也就是 nums[i] 自己一个元素作为子数组的情况
# 所以 dp(i) 只和 dp(i-1) 有关系，可以优化掉 dp 数组而只用几个变量

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
        return max(dp)


if __name__ == '__main__':
    nums = [5,4,-1,7,8]
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))