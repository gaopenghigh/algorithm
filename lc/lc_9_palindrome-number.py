# 9. 回文数
# 难度 简单
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 例如，121 是回文，而 123 不是。
# 
# 示例 1：
# 输入：x = 121
# 输出：true
# 
# 示例 2：
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 示例 3：
# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。


class Solution:
    # 转换为字符串
    def isPalindrome(self, x: int) -> bool:
        s = list(str(x))
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    # 纯数字处理，翻转后的数字应该和原数字相等
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        origin = x
        r = 0
        while x != 0:
            n = x % 10
            r = r*10 + n
            x = x // 10
        return r == origin

