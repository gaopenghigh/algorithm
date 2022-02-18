# 221. 最大正方形
# 难度 中等
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
# 
# 示例 1：
# 输入：matrix = [["1","0","1","0","0"],
#                ["1","0","1","1","1"],
#                ["1","1","1","1","1"],
#                ["1","0","0","1","0"]]
# 输出：4
# 
# 示例 2：
# 输入：matrix = [["0","1"],
#                ["1","0"]]
# 输出：1
# 
# 示例 3：
# 输入：matrix = [["0"]]
# 输出：0
#  
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] 为 '0' 或 '1'


# 求最值，考虑 DP
# dp[i][j] 表示以 matrix[i][j] 为右下角的只包含 1 的最大正方形的“边长”，则
# dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
# Base Case
# dp[0][j] = 1 if matrix[0][j] == '1' else 0
# dp[i][0] = 1 if matrix[i][0] == '1' else 0


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            if matrix[i][0] == '1':
                dp[i][0] = 1
        for j in range(cols):
            if matrix[0][j] == '1':
                dp[0][j] = 1
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        max_edge = 0
        for i in range(0, rows):
            for j in range(0, cols):
                max_edge = max(max_edge, dp[i][j])
        return max_edge * max_edge
