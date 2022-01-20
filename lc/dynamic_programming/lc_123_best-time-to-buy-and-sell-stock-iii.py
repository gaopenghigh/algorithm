# 123. 买卖股票的最佳时机 III
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 188 题的特殊形式, k = 2

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
        return self.dp(prices, days-1, 2, False)
