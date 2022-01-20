# 714. 买卖股票的最佳时机含手续费
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 返回获得利润的最大值。
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

# 188 题的特殊形式，k 为无穷大，但加入了手续费，状态转换方程需要改一下


import sys

class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def dp(self, prices, fee, x, have):
        if x == 0 and have:
            return -prices[x] - fee
        if x == 0 and not have:
            return 0
        
        if (x,have) in self.cache:
            return self.cache[(x,have)]
        
        if have:
            r = max(
                self.dp(prices, fee, x-1, True),
                self.dp(prices, fee, x-1, False) - prices[x] -fee
            )
            self.cache[(x,have)] = r
            return r
        else:
            r = max(
                self.dp(prices, fee, x-1, False),
                self.dp(prices, fee, x-1, True) + prices[x]
            )
            self.cache[(x,have)] = r
            return r


    def maxProfit(self, prices: list[int], fee: int) -> int:
        days = len(prices)
        if days == 0:
            return 0
        return self.dp(prices, fee, days-1, False)
