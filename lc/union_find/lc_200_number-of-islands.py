# 200. 岛屿数量
# 难度 中等
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 示例 1：
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 示例 2：
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        datas = []
        for row in range(rows):
            for col in range(cols):
                pos = (row, col)
                val = grid[row][col]
                if val == '1':
                    datas.append(pos)

        uf = UF(datas)
        for row in range(rows):
            for col in range(cols):
                pos = (row, col)
                val = grid[row][col]
                if val == '1':
                    up = (row-1, col)
                    down = (row+1, col)
                    left = (row, col-1)
                    right = (row, col+1)
                    for xy in [up, down, left, right]:
                        x, y = xy
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                            uf.union(pos, (x,y))
        return uf.count()

class UF:
    def __init__(self, datas):
        self.parents = {d : d for d in datas}
        self._count = len(datas)
    
    def find(self, x):
        if x not in self.parents:
            raise Exception()
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def connected(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        return rootX == rootY
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parents[rootX] = rootY
            self._count -= 1
    
    def count(self):
        return self._count
