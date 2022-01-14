# 785. 判断二分图
# 存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。给你一个二维数组 graph ，其中 graph[u] 是一个节点数组，由节点 u 的邻接节点组成。形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v 之间的无向边。该无向图同时具有以下属性：
# 不存在自环（graph[u] 不包含 u）。
# 不存在平行边（graph[u] 不包含重复值）。
# 如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
# 这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。
# 二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B 集合，就将这个图称为 二分图 。
# 
# 如果图是二分图，返回 true ；否则，返回 false 。

# 解法就是边遍历边染色，让邻接的顶点颜色不一样，如果染着染着发现做不到，说明不是二分图

COLOR_RED = "red"
COLOR_BLUE = "blue"

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        colors = {}
        for i in range(n):
            if i not in colors:
                if not self.isBiPartiteDFS(i, COLOR_RED, colors, graph):
                    return False
        return True

    def isBiPartiteDFS(self, u, color, colors, graph):
        colors[u] = color
        for v in graph[u]:
            # 已经涂过颜色，即已经遍历过
            if v in colors:
                if colors[u] == colors[v]:
                    return False
            else:
                color = COLOR_RED if colors[u] == COLOR_BLUE else COLOR_BLUE
                if not self.isBiPartiteDFS(v, color, colors, graph):
                    return False
        return True