# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 示例 1：
# 输入：s = "()"
# 输出：true
# 示例 2：
# 输入：s = "()[]{}"
# 输出：true
#
# 示例 3：
# 输入：s = "(]"
# 输出：false
#
# 示例 4：
# 输入：s = "([)]"
# 输出：false
#
# 示例 5：
# 输入：s = "{[]}"
# 输出：true
#  
# 
# 提示：
# 1 <= s.length <= 104
# s 仅由括号 '()[]{}' 组成

# 链接：https://leetcode-cn.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        t = {
            '{': '}',
            '[': ']',
            '(': ')',
        }
        for c in s:
            if c in ['[', '{', '(']:
                stack.append(c)
            else:
                if not stack:
                    return False
                left = stack.pop()
                if left not in t:
                    return False
                if t[left] != c:
                    return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    s = '{[](})'
    print(Solution().isValid(s))