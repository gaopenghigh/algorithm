# 130. 被围绕的区域
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 
# 使用并查集（https://blog.csdn.net/the_ZED/article/details/105126583），找到 4 条边上的 O，将他们和某个 dummy 连接起来，
# 然后逐个找剩下的格子，如果是 O，就与它的上下左右的格子连接起来，最后遍历一次所有格子，如果是 O 并且没有和 dummy 连接，则将它改为 X

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # build UnionFindSet
        m = len(board)
        n = len(board[0])
        dummy = (-1, -1)
        datas = [dummy]
        for i in range(m):
            for j in range(n):
                datas.append((i, j))
        uf = UF(datas)
        
        # 将 4 条边上的 O 和 dummy 连接
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    uf.union(dummy, (i, j))
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    uf.union(dummy, (i, j))
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                c = board[i][j]
                if c == 'O':
                    up = (i-1, j)
                    down = (i+1, j)
                    left = (i, j-1)
                    right = (i, j+1)
                    for xy in [up, down, left, right]:
                        x, y = xy
                        if board[x][y] == 'O':
                            uf.union((i, j), xy)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not uf.connected(dummy, (i, j)):
                    board[i][j] = 'X'


class UF:
    def __init__(self, datas) -> None:
        self.parents = {d : d for d in datas}
    
    def find(self, x) -> int:
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def connected(self, x, y) -> bool:
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return True
        return False

    def union(self, x, y) -> None:
        # print(f'union {x} to {y}')
        parent_x = self.find(x)
        parent_y = self.find(y)
        # print(f'parent of {x} is {parent_x}, parent of {y} is {parent_y}')
        if parent_x != parent_y:
            self.parents[parent_x] = parent_y


def test_uf():
    uf = UF([1, 2, 3, 4, 5])
    uf.union(2, 1)
    uf.union(2, 3)
    uf.union(4, 3)
    print(uf.connected(1, 4))
    print(uf.connected(2, 5))
    uf.union(5, 1)
    print(uf.connected(2, 5))

if __name__ == '__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    board = [["O","O"],["O","O"]]
    s = Solution()
    s.solve(board)
    print(board)
