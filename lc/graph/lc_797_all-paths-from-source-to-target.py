# 797. 所有可能的路径
# 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
# 二维数组的第 i 个数组中的单元都表示有向图中 i 号节点所能到达的下一些节点，空就是没有下一个结点了。
# 译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a 。

class Solution:
    def __init__(self) -> None:
        self.res = []

    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        path = []
        n = len(graph)
        self.dfs(graph, 0, n-1, path)
        return self.res
    
    def dfs(self, graph, src, dst, path):
        path.append(src)
        if src == dst:
            self.res.append(path[:])
            path.pop()
            return
        for adj in graph[src]:
            self.dfs(graph, adj, dst, path)
        path.pop()


# 也可以使用 BFS，只是放进队列的不是每一个节点，而是到达该节点的路径。
class SolutionBFS:
    def __init__(self) -> None:
        self.res = []

    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        self.bfs(graph, 0, n-1)
        return self.res

    def bfs(self, graph, src, dst):
        q = []
        path = [src]
        q.append(path)
        while len(q) > 0:
            path = q.pop(0)
            lastNode = path[-1]
            if lastNode == dst:
                self.res.append(path[:])
                continue
            else:
                for adj in graph[lastNode]:
                    newPath = path + [adj]
                    q.append(newPath)
        