# 62. 不同路径
# 难度 中等
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？
# 
# 示例 1：
# 输入：m = 3, n = 7
# 输出：28
# 
# 示例 2：
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
# 
# 示例 3：
# 输入：m = 7, n = 3
# 输出：28
# 
# 示例 4：
# 输入：m = 3, n = 3
# 输出：6


# 到达 matrix[i][j] 可以从 matrix[i-1][j] 或者从 matrix[i][j-1]，
# 考虑 DP, dp(i, j) 表示到达 matrix[i][j] 的路径数，则
# dp(i, j) = dp(i-1, j) + dp(i, j-1)
# base case
# dp(0, 0) = 1
# dp(x, 0) = 1
# dp(0, y) = 1

class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp(m-1, n-1)

    def dp(self, i, j):
        if i == 0 or j == 0:
            return 1
        if (i,j) in self.cache:
            return self.cache[(i,j)]
        r = self.dp(i-1, j) + self.dp(i, j-1)
        self.cache[(i,j)] = r
        return r
        
if __name__ == '__main__':
    m = 3
    n = 7
    print(Solution().uniquePaths(m, n))
