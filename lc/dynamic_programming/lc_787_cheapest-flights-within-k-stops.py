# 787. K 站中转内最便宜的航班
# 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。
# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。
# 
# 示例 1：
# 输入: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# 输出: 200

# 对于所有能抵达 dst 的城市 cities, price[i] 表示 cities[i] 到达 dst 的 价格，如果我们已经知道到在 k-1 站内到达 cities[i] 的最便宜价格，则也能知道 k 站内到达 dst 的最便宜价格了。
# 使用动态规划，dp(d, k) 表示在 k 次飞行之内从 src 到达 d 的最便宜价格，则
# dp(d, k) = min([dp(s, k-1) for s in "所有能到达 d 的城市")
# base case: dp(src, 1) = 0
# 注意 x 次中转代表能有 x + 1 次飞行

from collections import defaultdict
import sys

class Solution:
    def __init__(self) -> None:
        self.src = None
        self.dst = None
        self.flights_to = None
        self.cache = {}

    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        self.src = src
        self.dst = dst
        self.flights_to = defaultdict(lambda : [])
        for f in flights:
            start, end, p = f[0], f[1], f[2]
            self.flights_to[end].append((start, p))
        return self.dp(dst, k+1)
    
    # 经过 n 次飞行（n-1) 次中转从 self.src 到达 d 的最便宜票价和
    def dp(self, d, n):
        if d == self.src:
            return 0
        if n == 0:
            return -1
        if (d,n) in self.cache:
            return self.cache[(d,n)]
        min_price_to_d = sys.maxsize
        for start, price in self.flights_to[d]:
            sub_problem = self.dp(start, n-1)
            if sub_problem != -1:
                min_price_to_d = min(
                    min_price_to_d,
                    price + sub_problem
                )
        ans = min_price_to_d if min_price_to_d != sys.maxsize else -1
        self.cache[(d,n)] = ans
        return ans

if __name__ == '__main__':
    s = Solution()
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    print(s.findCheapestPrice(n, flights, src, dst, k))