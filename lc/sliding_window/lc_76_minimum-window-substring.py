# 76. 最小覆盖子串
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
# 
# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 
# 示例 2：
# 输入：s = "a", t = "a"
# 输出："a"
# 
# 示例 3:
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。

# 使用滑动窗口的思路

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        # 记录当前窗口中所需要的字符出现的
        window = defaultdict(lambda : 0)
        # 记录目前窗口中有多少个字符出现的子树与 t 的要求一样了
        valid = 0
        # 记录目前发现的最小子串
        shortest_substring_index = 0
        shortest_substring_len = -1
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            # 判断左边是否需要缩，如果当前窗口已经满足要求，左边就缩，一直缩到不满足为止
            while valid == len(need):
                # 发现了更小的字串
                if right - left < shortest_substring_len or shortest_substring_len == -1:
                    shortest_substring_index = left
                    shortest_substring_len = right - left
                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        
        if shortest_substring_len == -1:
            return ''
        return s[shortest_substring_index:shortest_substring_index + shortest_substring_len]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))