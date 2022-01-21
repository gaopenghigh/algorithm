# 121. 买卖股票的最佳时机
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

# 188 题的特殊形式

import sys

class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def dp(self, prices, x, y, have):
        if x == 0 and y >= 1 and have:
            return -prices[x]
        if x == 0 and not have:
            return 0
        if y == 0 and not have:
            return 0
        if y == 0 and have:
            return -sys.maxsize
        
        if (x,y,have) in self.cache:
            return self.cache[(x,y,have)]
        
        if have:
            r = max(
                self.dp(prices, x-1, y, True),
                self.dp(prices, x-1, y-1, False) - prices[x]
            )
            self.cache[(x,y,have)] = r
            return r
        else:
            r = max(
                self.dp(prices, x-1, y, False),
                self.dp(prices, x-1, y, True) + prices[x]
            )
            self.cache[(x,y,have)] = r
            return r

    def maxProfit(self, prices: list[int]) -> int:
        days = len(prices)
        if days == 0:
            return 0
        return self.dp(prices, days-1, 1, False)