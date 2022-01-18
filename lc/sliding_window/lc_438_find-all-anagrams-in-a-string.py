# 438. 找到字符串中所有字母异位词
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
# 
# 示例 1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 
#  示例 2:
# 
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        need = defaultdict(lambda : 0)
        for c in p:
            need[c] += 1
        window = defaultdict(lambda : 0)
        valid = 0
        left, right = 0, 0
        while right < len(p) - 1:
            if right >= len(s):
                return []
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            if valid == len(need):
                res.append(left)
            
            c = s[left]
            left += 1
            if c in need:
                if window[c] == need[c]:
                    valid -= 1
                window[c] -= 1
        return res

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))

    s = "abab"
    p = "ab"        
    print(Solution().findAnagrams(s, p))