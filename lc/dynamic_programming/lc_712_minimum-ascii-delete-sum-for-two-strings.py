# 712. 两个字符串的最小ASCII删除和
# 给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。
# 示例 1:
# 
# 输入: s1 = "sea", s2 = "eat"
# 输出: 231
# 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
# 在 "eat" 中删除 "t" 并将 116 加入总和。
# 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。

# 动态规划，删除后的最终结果肯定是最长子序列
# dp(i, j) 表示 s1[i:] 和 s2[j:] 这两个字符串需要变成最长子序列所需要删除的字符的 ASCII 值之和

class Solution:
    def __init__(self) -> None:
        self.s1 = ''
        self.s2 = ''
        self.cache = {}
    
    def dp(self, i, j):
        # base case 就是 s1 或 s2 为空字符串的情况，此时需要将另一个字符串的所有字符删掉
        if i == len(self.s1):
            return sum([ord(c) for c in self.s2[j:]])
        if j == len(self.s2):
            return sum([ord(c) for c in self.s1[i:]])
        
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        
        # s1[i] 和 s2[j] 相等，肯定在 LCS 中，不用删除
        if self.s1[i] == self.s2[j]:
            r = self.dp(i+1, j+1)
            self.cache[(i, j)] = r
            return r
        # s1[i] 和 s2[j] 不想等，至少有一个不在 LCS 中。
        # 注意，s1[i] 不在 LSC 的情况中，已经包含了 s2[j] 在 LCS 中，以及 s2[j] 不在 LCS 中这两种情况
        else:
            # s1[i] 不在 LCS 的情况，已经包含了 s2[j] 在 LCS 中，以及 s2[j] 不在 LCS 中这两种情况
            ri = ord(self.s1[i]) + self.dp(i+1, j)
            # s2[j] 不在 LCS 的情况，已经包含了 s1[i] 在 LCS 中，以及 s1[i] 不在 LCS 中这两种情况
            rj = ord(self.s2[j]) + self.dp(i, j+1)
            r = min(ri, rj)
            self.cache[(i, j)] = r
            return r

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        self.s1 = s1
        self.s2 = s2
        return self.dp(0, 0)

if __name__ == '__main__':
    s1 = "sea"
    s2 = "eat"
    print(Solution().minimumDeleteSum(s1, s2))