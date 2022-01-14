# 207. 课程表
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

# 抽象为判断一幅有向图是否有环

class Solution:
    def __init__(self) -> None:
        self.graph = []
        self.n = 0
    
    def _build_graph(self, n, edges):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for edge in edges:
            src, dst = edge[0], edge[1]
            self.graph[src].append(dst)
    
    def has_cycle_dfs(self, u, unsearched, searching):
        if u in searching:
            return True
        
        unsearched.remove(u)
        searching.add(u)

        for v in self.graph[u]:
            if v in searching:
                return True
            if v in unsearched:
                if self.has_cycle_dfs(v, unsearched, searching):
                    return True
        searching.remove(u)
        return False
    
    def has_cycle(self):
        unsearched = set()
        searching = set()
        for i in range(self.n):
            unsearched.add(i)

        for i in range(self.n):
            if i in unsearched:
                if self.has_cycle_dfs(i, unsearched, searching):
                    return True
        return False

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        self._build_graph(numCourses, prerequisites)
        # print(self.graph)
        return not self.has_cycle()


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))