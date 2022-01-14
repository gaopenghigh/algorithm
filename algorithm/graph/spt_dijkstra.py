# 最短路径树 SPT 的 Dijkstra 算法

import sys
from queue import PriorityQueue

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
    
    def _shortest_vertex_from_source(self, distTo, spt_vertices):
        min_weight = sys.maxsize
        min_vertex = None
        for v, weight in distTo.Items():
            if v not in spt_vertices and weight < min_weight:
                min_weight = weight
                min_vertex = v
        return min_vertex
    
    # 以 v 节点为源头生成 spt
    def spt(self, v):
        # distTo[i] 表示从 v 到 i 的最短路径
        distTo = {i : sys.maxsize for i in self.graph.keys()}
        distTo[v] = 0

        spt_vertices = []
        # 每次查一个顶点，len(self.graph) 次之后就能找到到所有顶点的最短路径了
        for _ in range(len(self.graph)):
            shortest_vertex = self._shortest_vertex_from_source(distTo)
            spt_vertices.append(shortest_vertex)
            for edge in self.graph[shortest_vertex]:
                _, adj, weight = edge
                if distTo[shortest_vertex] + weight < distTo[adj]:
                    distTo[adj] = distTo[shortest_vertex] + weight 
        return distTo

    # 另外一种方式是使用 BFS 的方式遍历所有节点，但队列需要使用优先级队列，权重值就是从源顶点到该顶点的距离（初始化为无穷大）。
    # 当遍历到到某个节点时，如果就能确定源节点到该节点的最短距离。
    # 如果是希望得到一个顶点到另外一个顶点的最短路径，则用这种方式能时间复杂度更低。
    def spt_bfs(self, v):
        distTo = {i : sys.maxsize for i in self.graph.keys()}
        pq = PriorityQueue()
        pq.put((0, v))
        distTo[v] = 0
        while len(pq) > 0:
            dist_to_curr_vertex, curr_vertex = pq.get()
            for edge in self.graph[curr_vertex]:
                _, adj, weight = edge
                if dist_to_curr_vertex + weight < distTo[adj]:
                    distTo[adj] = dist_to_curr_vertex + weight
                    pq.put((distTo[adj], adj))
        return distTo

    def shortest_path(self, v, target):
        distTo = {i : sys.maxsize for i in self.graph.keys()}
        pq = PriorityQueue()
        pq.put((0, v))
        distTo[v] = 0
        while len(pq) > 0:
            dist_to_curr_vertex, curr_vertex = pq.get()
            if curr_vertex == target:
                return dist_to_curr_vertex
            for edge in self.graph[curr_vertex]:
                _, adj, weight = edge
                if dist_to_curr_vertex + weight < distTo[adj]:
                    distTo[adj] = dist_to_curr_vertex + weight
                    pq.put((distTo[adj], adj))
        return distTo[target]
