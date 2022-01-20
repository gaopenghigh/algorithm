# 188. 买卖股票的最佳时机 IV
# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1：
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 示例 2：
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。


# 先注意一个点，一次“交易”指先买然后卖，所以只需要在“买”时扣除交易次数，“卖”时不需要。
# 每天都是能选择买还是卖，最终求的是最值，首先考虑使用动态规划。
# “选择”有 3 种：买、卖、不动
# “状态”需要能描述出过程中的子问题。
# 容易想到的有 2 个：天数、最多的交易次数，实际上还有第三个，就是手上有没有股票。一开始肯定是没有的，最后肯定也是卖掉的，但中间过程中，有些天会持有股票。
# 定义 dp 函数 dp(x, y, have) = m ，表示在 前 x 天内，在最多进行 y 次交易的限制下，并且第 x 天一定持有（have=True）或 不持有（have=False）的情况下，最大能获取的利益。
# 则
# dp(x, y, True) = max( dp(x-1, y, True),          dp(x-1, y-1, False) - prices[x])
#                       昨天就持有，今天什么也不做     昨天每持有，今天买的
# dp(x, y, False) = max( dp(x-1, y, False),        dp(x-1, y, True) + price[x])
#                       昨天就不持有，今天什么也不做    昨天持有，今天卖掉了
# base case:
# dp(0, y, True) = -price[0], (y>=1)
# dp(0, y, False) = 0
# dp(x, 0, False) = 0
# dp(x, 0, True) = -inf  (这种情况不会出现，所以设置为负无穷大)
# 最终需要求的是 dp(len(prices)-1, k, False)

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


    def maxProfit(self, k: int, prices: list[int]) -> int:
        days = len(prices)
        if days == 0:
            return 0
        return self.dp(prices, days-1, k, False)


if __name__ == '__main__':
    k = 2
    prices = [2,4,1]

    k = 2
    prices = [3,2,6,5,0,3]

    k = 2
    prices = []
    print(Solution().maxProfit(k, prices))