# 743. 网络延迟时间
# 有 n 个网络节点，标记为 1 到 n。
# 给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。
# 现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

# 寻找 SPT，寻找 SPT 中源节点到所有其他节点的距离的最大值，Dijkstra 算法。
# 使用邻接矩阵表示法

import sys

class Graph:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
    
    def _min_dist_v_from_spt(self, spt_vertices, dist_to):
        min_dist = sys.maxsize
        min_dist_v = None
        for v, dist in dist_to.items():
            if v not in spt_vertices:
                if dist < min_dist:
                    min_dist = dist
                    min_dist_v = v
        return min_dist_v
    
    def adjs(self, v):
        adjs = []
        for i in range(0, len(self.matrix)):
            weight = self.matrix[v][i]
            if weight >= 0:
                adjs.append((i, weight))
        return adjs
    
    def spt(self, source):
        dist_to = {v : sys.maxsize for v in range(len(self.matrix))}
        dist_to[source] = 0
        spt_vertices = set()
        for _ in range(len(self.matrix)):
            v = self._min_dist_v_from_spt(spt_vertices, dist_to)
            spt_vertices.add(v)
            if v is None:
                return None
            for adj in self.adjs(v):
                adj_v, adj_weight = adj
                if dist_to[v] + adj_weight < dist_to[adj_v]:
                    dist_to[adj_v] = dist_to[v] + adj_weight
        return dist_to


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        matrix = [[-1 for _ in range(n)] for _ in range(n)]
        for e in times:
            src, dst, weight = e
            matrix[src-1][dst-1] = weight
        g = Graph(matrix)
        dist_to = g.spt(k-1)
        if dist_to is None:
            return -1
        return max(dist_to.values())


if __name__ == '__main__':
    times = [[1,2,1]]
    n = 2
    k = 2
    s = Solution()
    print(s.networkDelayTime(times, n, k))
