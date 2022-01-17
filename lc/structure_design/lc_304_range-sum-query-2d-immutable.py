# 304. 二维区域和检索 - 矩阵不可变
# 给定一个二维矩阵 matrix，以下类型的多个请求：
# 计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
# 实现 NumMatrix 类：
# NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
# int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、右下角 (row2, col2) 所描述的子矩阵的元素 总和 。

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# 使用前缀和的思路， pre[i][j] 表示 左上角为 (0,0)，右下角 (i-1, j-1)的矩形内元素的和

class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.pre = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.pre[i][j] = self.pre[i-1][j] + self.pre[i][j-1] + matrix[i-1][j-1] - self.pre[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre[row2+1][col2+1] - self.pre[row1][col2+1] - self.pre[row2+1][col1] + self.pre[row1][col1] 
