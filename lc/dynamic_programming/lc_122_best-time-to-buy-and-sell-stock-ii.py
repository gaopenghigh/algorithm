# 122. 买卖股票的最佳时机 II
# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 188 题的特殊形式，相当于 k 为无穷大，也就是无需考虑 k 的因素，直接拿掉就好

class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def dp(self, prices, x, have):
        if x == 0 and have:
            return -prices[x]
        if x == 0 and not have:
            return 0
        
        if (x,have) in self.cache:
            return self.cache[(x,have)]
        
        if have:
            r = max(
                self.dp(prices, x-1, True),
                self.dp(prices, x-1, False) - prices[x]
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