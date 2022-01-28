# 54. 螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]

# 可以将矩阵看成若干层，首先输出最外层的元素，其次输出次外层的元素，直到输出最内层的元素。
# 处理这类问题，在写出基本算法后，需要着重考虑一下边界条件，比如空矩阵、只有一个元素矩阵，只有一行的矩阵比如 [[1,2,3]]，只有一列的矩阵比如 [[1],[2],[3]]等等

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix) == 0:
            return []
        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for col in range(left, right+1):
                res.append(matrix[top][col])
            for row in range(top+1, bottom+1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right-1, left-1, -1):
                    res.append(matrix[bottom][col])
                for row in range(bottom-1, top, -1):
                    res.append(matrix[row][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return res

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().spiralOrder(matrix))