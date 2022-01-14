# 990. 等式方程的可满足性
# 给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
# 只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

# 使用并查集，a==b 表示 a 和 b 连通， a!=b 表示 a 和 b 不连通。

class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        datas = set()
        for e in equations:
            x, y = e[0], e[3]
            datas.add(x)
            datas.add(y)
        uf = UF(list(datas)) 
        for e in equations:
            x, o, y = e[0], e[1:3], e[3]
            if o == '==':
                uf.union(x, y)
        for e in equations:
            x, o, y = e[0], e[1:3], e[3]
            if o == '!=':
                if uf.connected(x, y):
                    return False
        return True

class UF:
    def __init__(self, datas) -> None:
        self.parents = {d : d for d in datas}
        # 联通分量数
        self.count = len(datas)
    
    def find(self, x):
        if x not in self.parents:
            return None
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def connected(self, x, y) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        return root_x == root_y
    
    def union(self, x, y) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parents[root_y] = root_x
