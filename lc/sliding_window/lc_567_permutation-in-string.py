# 567. 字符串的排列
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
# 换句话说，s1 的排列之一是 s2 的 子串 。
# 
# 示例 1：
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
# 
# 示例 2：
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
 

# 滑动窗口，只是窗口的大小是固定的

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = defaultdict(lambda : 0)
        for c in s1:
            need[c] += 1
        window = defaultdict(lambda : 0)
        valid = 0
        left = 0
        right = 0
        while right < len(s1)-1:
            if right >= len(s2):
                return False
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if need[c] == window[c]:
                    valid += 1
        while right < len(s2):
            # print(f'left={left}, right={right}, window={window}, valid={valid}')
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if need[c] == window[c]:
                    valid += 1

            if valid == len(need):
                return True
            c = s2[left]
            left += 1
            if c in need:
                if need[c] == window[c]:
                    valid -= 1
                window[c] -= 1

        return False

if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1, s2))

    s1= "ab"
    s2 = "eidboaoo"
    print(Solution().checkInclusion(s1, s2))

    s1 = "adc"
    s2 = "dcda"
    print(Solution().checkInclusion(s1, s2))

    s1 = "a"
    s2 = "ab"
    print(Solution().checkInclusion(s1, s2))

    s1 = "horse"
    s2 = "ros"
    print(Solution().checkInclusion(s1, s2))