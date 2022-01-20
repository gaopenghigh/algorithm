# 309. 最佳买卖股票时机含冷冻期
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 示例:
# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

# 188 题的特殊形式， k 为无穷大（也就是没有影响），但有冷冻期，状态转移方程需要改一下
# base case 也需要改一下，由于需要 2 天前的情况，所以 x == 0 和 x == 1 的 base case 需要直接算出来

import sys

class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def dp(self, prices, x, have):
        if x == 0 and have:
            return -prices[x]
        if x == 0 and not have:
            return 0
        if x == 1 and not have:
            return max(
                prices[1] - prices[0],   # day0 买 day1 卖
                0,  # 没买没卖
            )
        if x == 1 and have:
            return max(
                -prices[0],
                -prices[1]
            )
        
        if (x,have) in self.cache:
            return self.cache[(x,have)]
        
        if have:
            r = max(
                self.dp(prices, x-1, True),
                self.dp(prices, x-2, False) - prices[x]
            )
            self.cache[(x,have)] = r
            return r
        else:
            r = max(
                self.dp(prices, x-1, False),
                self.dp(prices, x-1, True) + prices[x]
            )
            self.cache[(x,have)] = r
            return r


    def maxProfit(self, prices: list[int]) -> int:
        days = len(prices)
        if days == 0:
            return 0
        return self.dp(prices, days-1, False)

if __name__ == '__main__':
    prices = [1,2,3,0,2]
    print(Solution().maxProfit(prices))