# 1584. 连接所有点的最小费用
# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。

# 抽象为计算图的最小生成树 MST

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        g = Graph()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                x1, y1 = p1[0], p1[1]
                x2, y2 = p2[0], p2[1]
                weight = abs(x1-x2) + abs(y1-y2)
                edge = (i, j, weight)
                g.add_edge(edge)
        
        mst_edges = g.mstEdges()
        return sum([e[2] for e in mst_edges])


class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_edge(self, e: tuple):
        # edge is tuple: (src, dst, weight)
        # 无向图，所以实际上需要添加 2 条边
        src, dst, weight = e
        if src in self.graph:
            self.graph[src].append(e)
        else:
            self.graph[src] = [e]
        if dst in self.graph:
            self.graph[dst].append((dst, src, weight))
        else:
            self.graph[dst] = [(dst, src, weight)]
    
    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
    
    def mstEdges(self):
        mst_edges = set()

        all_edges = []
        for edges in self.graph.values():
            all_edges.extend(edges)
        # 按照权重从小到大排序
        all_edges.sort(key=lambda x : x[2])

        # 构建并查集
        uf = UF([v for v in self.graph.keys()])

        for edge in all_edges:
            src, dst, _ = edge
            if not uf.connected(src, dst):
                mst_edges.add(edge)
                uf.union(src, dst)
        return mst_edges

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