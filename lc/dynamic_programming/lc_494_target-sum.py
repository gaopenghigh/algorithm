# 494. 目标和
# 给你一个整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
# 
# 示例 1：
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 
# 示例 2：
# 输入：nums = [1], target = 1
# 输出：1
#
# 提示：
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000


# 使用回溯算法

class Solution1:
    def __init__(self) -> None:
        self.nums = None
        self.ans = 0
    
    def backtrack(self, i, rest):
        if i == len(self.nums):
            if rest == 0:
                self.ans += 1
            return
        
        # +
        rest = rest - self.nums[i]
        self.backtrack(i + 1, rest)
        rest = rest + self.nums[i]
        # -
        rest = rest + self.nums[i]
        self.backtrack(i + 1, rest)
        rest = rest - self.nums[i]
        

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        self.nums = nums
        self.backtrack(0, target)
        return self.ans

# 没办法直接使用动态规划，如果可以，
# dp[i][j] 中的 i 和 j 表示状态：从前 i 个元素中选择，target 为 j 的不同表达式的数目
# 由于元素都 >=0，所以 j 的取值范围为 [-sum(nums), sum(nums)]，可能为负数，所以用 {}
# base case 为 dp[0][0] = 1，dp[0][j] = 0，dp[i][0] 
# 计算 dp[i][j]，对于 nums[i]，要么是添加 + 要么是添加 -
# 1. 添加 +，则 dp[i][j] = dp[i-1][j-nums[i]]
# 2. 添加 -，则 dp[i][j] = dp[i-1][j+nums[i]]
# 显然 dp table 中 dp[i][j] 的值不能通过之前已经算出来的结果或者 base case 计算的到，而这又是因为 '-' 的引入。
#
# 有没有办法可以不要引入 '-' 呢。
# 可以想象把数字分别装入两个背包中，背包 A 的数字添加 '+'，背包 B 中的数字添加 '-'，则：
# sum(A) - sum(B) = target
# 我们指向关注 A，而 sum(B) = sum - sum(A)，所以
# sum(A) - sum + sum(A) = target
# sum(A) = (target + sum) / 2
# 现在问题就变成了，从 nums 中挑选数字放进一个背包，多少中办法可以让背包中的数字总和刚好为 (target+sum)/2
# 使用 dp[i][j] = x，其中 i 表示从前 i 个数字中选择，j 表示数字总和为 j，x 表示方法数
# i 的取值范围为 [0, len(nums)]，j 的取值范围为 [0, (target+sum)/2]
# base case: dp[0][0] = 1，dp[0][j] | j > 0 为 0
# dp[i][j] 的计算，对应任意一个数字，要么选要么不选，所以
# 1. 选，dp[i][j] = dp[i-1][j-nums[i-1]]
# 2. 不选，dp[i][j] = dp[i-1][j]
# 所以 dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if (target + total) % 2 != 0:
            return 0
        if total < target:
            return 0
        need = (target + total) // 2
        if need < 0:
            return 0
        dp = [[0 for _ in range(need+1)] for _ in range(len(nums)+1)]
        for j in range(1, need+1):
            dp[0][j] = 0
        dp[0][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(0, need+1):
                # 可以选或者不选
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                # 只能不选
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][need]



if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1,1]
    target = 3
    # nums = [0,0,0,0,0,0,0,0,1]
    # target = 1
    nums = [100]
    target = -200
    print(s.findTargetSumWays(nums, target))