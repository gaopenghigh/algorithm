# 72. 编辑距离
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 示例 1：
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')

# 动态规划。
# 先考虑 base case，当 word1 或 word2 为空字符串时，那需要的操作就是把另外一个字符串的所有字符都删除掉。
# 用 dp[0][0] 表示两个都是空字符串的情况，显然 dp[0][0] = 0，dp[0][j] = j, dp[i][0] = i
# 用 dp[i][j] 表示 word1[0:i-1] 和 word[0:j-1] 的最小编辑距离。
# 
# 怎么算出 word[i:] 和 word[j:] 的编辑距离呢？
# 如果 word1[i] == word2[j]，那这两个字符就不需要编辑，也就是最小编辑距离不变
# 如果 word1[i] != word2[j]，则我们可以用插入、删除、替换 3 中方式的一种对它进行操作:
# 1. 插入
#    插入在 i 后面新增一个字符 c，并且 c = word2[j]，由于
#    minDistance(word1[0:i] + c, word2[0:j]) == minDistance(word1[0:i], word2[0:j-1])
#    所以： dp[i][j] = 1 + dp[i][j-1]
# 2. 删除
#    删除 word1[i] 的字符，则
#    dp[i][j] = 1 + dp[i-1][j]
# 3. 替换
#    word1[i] 的值替换为 c，其中 c == word2[j]，由于
#    minDistance(word1[:i-1] + c, word2[:j]) == minDistance(word1[:i-1], word2[:j-1])
#    所以 dp[i][j] = 1 + dp[i-1] + dp[j-1]
# 最后从 3 中操作后得到的最小编辑距离中去最小的一种编辑方式即可得到 dp[i][j] 的值


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        # base case
        dp[0][0] = 0
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        1 + dp[i][j-1],
                        1 + dp[i-1][j],
                        1 + dp[i-1][j-1],
                    )
        return dp[len(word1)][len(word2)]

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))