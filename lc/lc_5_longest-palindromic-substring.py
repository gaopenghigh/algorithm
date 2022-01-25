# 5. 最长回文子串
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"
# 
# 示例 3：
# 输入：s = "a"
# 输出："a"
# 
# 示例 4：
# 输入：s = "ac"
# 输出："a"


# 技巧是以每一个字符为中心，向两边拓展，看最大能组成多大的回文字串。
# 但回文字符串长度可能为偶数，所以算法思路为：
# for i in range(0, len(s)):
#     找到以 s[i] 为中心的回文字符串，
#     找到以 s[i] 和 s[i+1] 为中心的回文字符串
#     更新答案


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(0, len(s)):
            r = self.findPalindrome(s, i, i)
            if len(r) > len(res):
                res = r
            r = self.findPalindrome(s, i, i+1)
            if len(r) > len(res):
                res = r
        return res

    def findPalindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left+1:right-1+1]

if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))