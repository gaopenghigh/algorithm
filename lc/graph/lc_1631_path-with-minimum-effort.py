# 1631. 最小体力消耗路径
# 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。
# 一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
# 请你返回从左上角走到右下角的最小 体力消耗值 。

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
    
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        g = self._build_graph(heights)

        start = (0,0)
        rows = len(heights)
        cols = len(heights[0])
        end = (rows-1, cols-1)

        effortTo = {i : sys.maxsize for i in g.graph.keys()}
        pq = PriorityQueue()
        pq.put((0, start))
        effortTo[start] = 0
        while not pq.empty():
            effort_to_curr_vertex, curr_vertex = pq.get()
            if curr_vertex == end:
                return effort_to_curr_vertex
            for edge in g.graph[curr_vertex]:
                _, adj, effort = edge
                if max(effort_to_curr_vertex, effort) < effortTo[adj]:
                    effortTo[adj] = max(effort_to_curr_vertex, effort)
                    pq.put((effortTo[adj], adj))
        return effortTo[end]
    
    def _build_graph(self, heights):
        g = Graph()
        rows = len(heights)
        cols = len(heights[0])
        for i in range(0, rows):
            for j in range(0, cols):
                v = (i, j)
                up = (i-1, j)
                down = (i+1, j)
                left = (i, j-1)
                right = (i, j+1)
                for adj in [up, down, left, right]:
                    if adj[0] < 0 or adj[0] > rows - 1:
                        continue
                    if adj[1] < 0 or adj[1] > cols - 1:
                        continue
                    effort = abs(heights[i][j] - heights[adj[0]][adj[1]])
                    g.add_edge((v, adj, effort))
        return g


if __name__ == '__main__':
    pass