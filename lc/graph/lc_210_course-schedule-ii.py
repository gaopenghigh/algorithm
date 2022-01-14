# 210. 课程表 II
# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。
# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。

# DAG 的拓扑排序
# 准备一个栈，做深度优先搜索，在搜索完一个顶点后，将该顶点压入栈中（此时该顶点所有可达的顶点已经在栈中了）。最后逐个弹出栈中元素。

class Solution:
    def __init__(self) -> None:
        self.graph = []
        self.n = 0
        self.has_cycle = False
    
    def _build_graph(self, n, edges):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for edge in edges:
            src, dst = edge[0], edge[1]
            self.graph[src].append(dst)
    
    def _dfs(self, u, unsearched, searching, stack):
        # print(f'u={u}, unsearched={unsearched}, searching={searching}, stack={stack}')
        unsearched.remove(u)

        if u in searching:
            self.has_cycle = True
            return

        searching.add(u)

        for v in self.graph[u]:
            if v in searching:
                self.has_cycle = True
                return
            if v in unsearched:
                self._dfs(v, unsearched, searching, stack)
                if self.has_cycle:
                    return
        
        searching.remove(u)
        stack.append(u)

    def topological_sort(self):
        unsearched = set()
        searching = set()
        stack = []
        for i in range(self.n):
            unsearched.add(i)

        for i in range(self.n):
            if i in unsearched:
                self._dfs(i, unsearched, searching, stack)
                if self.has_cycle:
                    return []

        ret = []
        while len(stack) > 0:
            ret.append(stack.pop())
        return ret

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        self._build_graph(numCourses, prerequisites)
        r = self.topological_sort()
        return r[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(3, [[0,2], [2, 1], [0, 1]]))