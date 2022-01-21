# 213. 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
# 
# 示例 1：
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 
# 示例 2：
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 3：
# 输入：nums = [1,2,3]
# 输出：3

# 类似 198，加上一些限制条件，针对第一间和最后一间，只有 3 中情况：
# 1. 抢了第 1 间没抢最后一间，则第 2 间不能抢，得到的是金额是 nums[0] + 对第 3 间到倒数第二间进行行动所得的金额
# 2. 抢了最后一间没抢第 1 间，则倒数第二间不能抢，得到的金额是 nums[len-1] + 对第 2 间到倒数第 3 间进行行动所得的金额
# 3. 第 1 间和最后一间都没抢，得到的金额是 对第 2 间到倒数第 2 间进行行动所得的金额
# dp(i, j) = x 表示对第 i 间到 第 j 间进行行动，并且不用考虑首尾问题时能得到的最大金额，则
# 最终答案就是 max( nums[0] + dp(3, len-1),  nums[len-1] + dp(2, len-2), dp(2, len-1))
# dp(i, j) = max(nums[j-1] + dp(i, j-2), dp(i, j-1))
# base case:
# dp(x, 0) = 0，dp(x, y) = 0 (y<x) 表示没有房间可以抢
# dp(x, x) = nums[x-1]


class Solution:
    def __init__(self) -> None:
        self.cache = {}
    
    def dp(self, nums, i, j):
        if j == 0:
            return 0
        if j < i:
            return 0
        if i == j:
            return nums[i-1]
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        r = max(
            nums[j-1] + self.dp(nums, i, j-2),
            self.dp(nums, i, j-1)
        )
        self.cache[(i, j)] = r
        return r
        
    def rob(self, nums: list[int]) -> int:
        length = len(nums)
        return max(
            nums[0] + self.dp(nums, 3, length-1),
            nums[length-1] + self.dp(nums, 2, length-2),
            self.dp(nums, 2, length-1)
        )

if __name__ == '__main__':
    nums = [1,2,3,1]
    print(Solution().rob(nums))
