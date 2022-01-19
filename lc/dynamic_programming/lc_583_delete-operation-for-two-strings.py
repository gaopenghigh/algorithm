# 583. 两个字符串的删除操作
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
# 示例：
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

# 最终两个字符串就是会变成两个字符串的最长子序列，和 1143 题差不多
# 使用”自顶向下“的递归 dp 函数的方式
# dp(i, j) 表示 word1[i:] 和 word2[j:] 的最长子序列的长度

class Solution:
    def __init__(self) -> None:
        self.word1 = ''
        self.word2 = ''
        self.cache = {}

    def dp(self, i, j):
        # 其中一个是空字符串
        if i == len(self.word1) or j == len(self.word2):
            return 0
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        # word[1] 和 word2[j] 一样，该字符肯定在最长子序列中
        if self.word1[i] == self.word2[j]:
            r = 1 + self.dp(i+1, j+1)
            self.cache[(i,j)] = r
            return r
        # word[1] 或 word2[j] 中的一个不在最长子序列中
        else:
            r = max(self.dp(i+1, j), self.dp(i, j+1) )
            self.cache[(i,j)] = r
            return r


    def minDistance(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        lcs = self.dp(0, 0)
        return len(word1) - lcs + len(word2) - lcs


if __name__ == '__main__':
    s = Solution()
    w1 = 'sea'
    w2 = 'eat'
    print(s.minDistance(w1, w2))