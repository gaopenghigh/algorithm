# 48. 旋转图像
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
# 
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]
# 
# 示例 2：
# 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# 
# 示例 3：
# 输入：matrix = [[1]]
# 输出：[[1]]
# 
# 示例 4：
# 输入：matrix = [[1,2],[3,4]]
# 输出：[[3,1],[4,2]]
# 
# 提示：
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
# 

# 解法参考 https://leetcode-cn.com/problems/rotate-image/solution/xuan-zhuan-tu-xiang-by-leetcode-solution-vu3m/
# 直观的解法是从数学上总结出矩阵旋转后的规律，然后创建一个新的矩阵存储翻转后的值。
# 题目要求不要使用另一个矩阵，技巧点（套路）是使用两次翻转（一次水平翻转和一次对角线翻转）来代替旋转。但翻转的技巧并不直观，需要记忆这个技巧。

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        # 对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]