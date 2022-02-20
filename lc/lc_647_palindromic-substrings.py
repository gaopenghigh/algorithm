# 647. 回文子串
# 难度 中等
# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
# 回文字符串 是正着读和倒过来读一样的字符串。
# 子字符串 是字符串中的由连续字符组成的一个序列。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
# 
# 示例 1：
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 
# 示例 2：
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for idx, c in enumerate(s):
            # 总字符为奇数
            i = 0
            while idx - i >= 0 and idx + i < len(s):
                if s[idx-i] == s[idx+i]:
                    count += 1
                else:
                    break
                i += 1
            # 总字符为偶数
            left = idx - 1
            right = idx
            i = 0
            while left - i >= 0 and right + i < len(s):
                if s[left-i] == s[right+i]:
                    count += 1
                else:
                    break
                i += 1
        return count