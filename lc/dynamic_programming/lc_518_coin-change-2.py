# 518. 零钱兑换 II
# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
# 假设每一种面额的硬币有无限个。 
# 题目数据保证结果符合 32 位带符号整数。
# 
# 示例 1：
# 输入：amount = 5, coins = [1, 2, 5]
# 输出：4
# 解释：有四种方式可以凑成总金额：
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 示例 2：
# 输入：amount = 3, coins = [2]
# 输出：0
# 解释：只用面额 2 的硬币不能凑成总金额 3 。
# 
# 示例 3：
# 输入：amount = 10, coins = [10] 
# 输出：1

# dp[i][j] 中的 i 和 j 描述一个局面，表示使用前 i 中面额的硬币凑出总金额为 j 的方法数。
# base case 为:
#     dp[x][0] = 1
#     dp[0][x] = 0, x > 0

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for j in range(1, amount+1):
            dp[0][j] = 0

        for i in range(1, len(coins) + 1):
            for j in range(1, amount+1):
                coin = coins[i-1]
                if j >= coin:
                # 可以使用 coin 面额的硬币或者不使用
                    dp[i][j] = dp[i][j-coin] + dp[i-1][j]
                # 只能不使用
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(coins)][amount]



if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))