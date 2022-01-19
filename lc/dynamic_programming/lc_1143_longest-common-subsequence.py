# 1143. 最长公共子序列
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
# 
# 示例 1：
# 输入：text1 = "abcde", text2 = "ace" 
# 输出：3  
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
# 
# 示例 2：
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
# 
# 示例 3：
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。

# 动态规划。
# 基本情况是，如果某个字符串是空字符串，则最长公共子序列长度肯定为 0
# 用 dp[0][0] 表示 两个字符串都为空字符串的情况，dp[i][j] 表示 text1[0:i-1] 和 text2[0:j-1] 的最长公共子序列的长度
 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        # 针对 text1 和 teext2 的每一个字符，考虑它是否在最长子序列中
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                # text[1] 和 text2[j] 肯定在最长子序列中
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # text[1] 或 text2[j] 中的某一个不在最长子序列中
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(text1)][len(text2)]
                
if __name__ == '__main__':
    s = Solution()
    t1 = 'abc'
    t2 = 'ac'
    print(s.longestCommonSubsequence(t1, t2))