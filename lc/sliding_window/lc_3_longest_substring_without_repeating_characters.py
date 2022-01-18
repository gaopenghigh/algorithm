# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
# 
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
# 示例 2:
# 
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
# 示例 3:
# 
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
# 示例 4:
# 输入: s = ""
# 输出: 0
# 
# 提示：
# 0 <= s.length <= 5 * 104
# s 由英文字母、数字、符号和空格组成
# 
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters

# 使用滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ans = 0, 0, 0
        used_char = set()
        n = len(s)
        while r < n:
            c = s[r]
            # print(f'l={l} r={r} c={c} used_char={used_char} ans={ans}')
            if c in used_char:
                used_char.remove(s[l])
                l += 1
            else:
                used_char.add(c)
                if r - l + 1 > ans:
                    ans = r - l + 1
                r += 1
            # print(f'l={l} r={r} c={c} used_char={used_char} ans={ans}')
        return ans


# 使用滑动窗口，优化的点在于发现重复字符后，左指针不用一步一步右移，而是可以直接移动到该重复字符上一次出现的位置。
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        pos = {}
        ans = 0
        n = len(s)
        while r < n:
            c = s[r]
            # print(f'l={l} r={r} c={c} pos={pos} ans={ans}')
            if c in pos and l <= pos[c]:
                l = pos[c] + 1
            else: # c not in pos or l > pos[c]
                if r - l + 1 > ans:
                    ans = r - l + 1
            pos[c] = r
            r += 1
        return ans


if __name__ == '__main__':
    s = "abcabcbb"
    print(s, Solution().lengthOfLongestSubstring(s))
    s = "bbbbb"
    print(s, Solution().lengthOfLongestSubstring(s))
    s = "pwwkew"
    print(s, Solution().lengthOfLongestSubstring(s))
    s = ""
    print(s, Solution().lengthOfLongestSubstring(s))
    s = "aab"
    print(s, Solution().lengthOfLongestSubstring(s))
    s = "tmmzuxt"
    print(s, Solution().lengthOfLongestSubstring(s))