# 886. 可能的二分法
# 给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。
# 每个人都可能不喜欢其他人，那么他们不应该属于同一组。
# 形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。
# 当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。

# 同 785，即判断是否为二分图

COLOR_RED = "red"
COLOR_BLUE = "blue"

class Solution:
    def __init__(self) -> None:
        self.graph = []
        self.n = 0
    
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        # build graph
        self.n = n
        self.graph = [[] for _ in range(n)]
        for dislike in dislikes:
            src, dst = dislike[0] - 1, dislike[1] - 1
            self.graph[src].append(dst)
            self.graph[dst].append(src)
        return self.isBiPartitite()
    
    def isBiPartitite(self):
        colors = {}
        for i in range(self.n):
            if i not in colors:
                if not self._isBiPartiteDFS(i, COLOR_RED, colors):
                    return False
        return True
    
    def _isBiPartiteDFS(self, u, color, colors):
        colors[u] = color
        for v in self.graph[u]:
            if v in colors:
                if colors[v] == colors[u]:
                    return False
            else:
                colorV = COLOR_BLUE if colors[u] == COLOR_RED else COLOR_RED
                if not self._isBiPartiteDFS(v, colorV, colors):
                    return False
        return True
