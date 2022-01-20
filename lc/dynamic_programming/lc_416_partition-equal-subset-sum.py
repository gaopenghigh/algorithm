# 416. 分割等和子集
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 示例 1：
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。

# 背包问题的变形： 从 nums 中挑选元素，能否刚好放满容量为 sum(nums)/2 的一个背包

# 动态规划第一步要明确两点，「状态」和「选择」。
# 状态就是对一个局面的描述。只要给定几个可选物品和一个背包的容量限制，就形成了一个背包问题，对不对？所以状态有两个，就是「背包的容量」和「可选择的物品」。
# 再说选择，也很容易想到啊，对于每件物品，你能选择什么？选择就是「装进背包」或者「不装进背包」嘛。
# 动态规划的框架如下：
# for 状态1 in 状态1的所有取值：
#     for 状态2 in 状态2的所有取值：
#         for ...
#             dp[状态1][状态2][...] = 择优(选择1，选择2...)

# dp[i][j] 中的 i 和 j 就可以描述一个局面：从前 i 个元素挑选，刚好能装满容量为 j 的背包
# base case 就是可选的元素为空，或者背包容量为 0，也就是 dp[0][x] = False, dp[x][0] = True（背包没有用空间的时候，相当于装满了）
# 对于一个索引为 i 的元素，它的“重量”为 nums[i]，要么放进背包，要么不放。
# 如果放进背包，则 dp[i][j] = dp[i-1][j-nums[i]] == True
# 如果不放进背包，则 dp[i][j] = dp[i-j][j] == True
# 针对上面两种情况，只要不都为 False ，则 dp[i][j] 就位 True

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        # 总和为奇数肯定不行
        if total % 2 != 0:
            return False
        half = total // 2
        dp =[[False for _ in range(half + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, half + 1):
                # 放不进去
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j] is True
                else:
                    dp_in = dp[i-1][j-nums[i-1]] is True
                    dp_not_in = dp[i-1][j] is True
                    dp[i][j] = dp_in or dp_not_in
        return dp[len(nums)][half]

if __name__ == '__main__':
    nums = [1,5,11,5]
    # nums = [1, 2, 5]
    print(Solution().canPartition(nums))