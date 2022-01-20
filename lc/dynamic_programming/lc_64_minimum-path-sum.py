# 64. 最小路径和
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
#示例 1：
#输入：grid = [[1,3,1],
#             [1,5,1],
#             [4,2,1]]
#输出：7
#解释：因为路径 1→3→1→1→1 的总和最小。
#
#示例 2：
#输入：grid = [[1,2,3],
#             [4,5,6]]
#输出：12

# 要到达 grid[i][j] 只能通过其上面格子或者左边格子，如果以及知道到达上面格子或者左边格子的最小路径和，显然其中的较小值加上 grid[i][j] 的值就是最终答案
# 使用动态规划，描述某个时刻的状态，我们仅需要知道当前走到了哪个位置
# dp[i][j] 表示走到 grid[i][j] 的最小路径和
# 则 dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
# base case:
#     dp[0][0] = grid[0][0]
#     dp[0][x] = sum(grid[0][0:x])
#     dp[x][0] = sum(grid[0:x][0])

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[None for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for j in range(1, cols):
            dp[0][j] = sum(grid[0][:j+1])
        for i in range(1, rows):
            dp[i][0] = sum([grid[x][0] for x in range(i+1)])
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
        return dp[rows-1][cols-1]

if __name__ == '__main__':
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    print(Solution().minPathSum(grid))

