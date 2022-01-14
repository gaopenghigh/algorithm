# 最小生成树的 Kruskal 算法
# 使用邻接表实现图

import sys

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

if __name__ == '__main__':
    g = Graph()
    g.add_edge((0, 1, 10))
    g.add_edge((0, 2, 6))
    g.add_edge((0, 3, 5))
    g.add_edge((1, 3, 15))
    g.add_edge((2, 3, 4))

    mstEdges = g.mstEdges()
    for e in mstEdges:
        print(e)