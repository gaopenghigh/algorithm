# 最小生成树的 Prime 算法
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
    
    def _min_weight_edge_from_mst_set(self, mst_vertex_set, edges_from_mst_vertices):
        min_weight = sys.maxsize
        min_weight_edge = None
        for e in edges_from_mst_vertices:
            dst, weight = e[1], e[2]
            if dst not in mst_vertex_set:
                if weight < min_weight:
                    min_weight = weight
                    min_weight_edge = e
        return min_weight_edge
    
    # 返回组成 MST 的边的列表
    def mstEdges(self) -> list[tuple]:
        mst_vertex_set = set()
        mst_edges_set = set()
        edges_from_mst_vertices = []
        all_vertices = set(self.graph.keys())

        v = all_vertices.pop()
        mst_vertex_set.add(v)
        edges_from_mst_vertices.extend(self.graph[v])
        # 每次寻找一个顶点，由于 v 已经寻找完成，所以如果能找到 mst 的话，再寻找 len(self.graph) - 1 次就能找完
        for _ in range(len(self.graph) - 1):
            min_weight_edge = self._min_weight_edge_from_mst_set(mst_vertex_set, edges_from_mst_vertices)
            if min_weight_edge is None:
                # 找不到，说明图不是全连通的
                return None
            mst_vertex_set.add(min_weight_edge[1])
            edges_from_mst_vertices.extend(self.graph[min_weight_edge[1]])
            mst_edges_set.add(min_weight_edge)
        return mst_edges_set
        

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