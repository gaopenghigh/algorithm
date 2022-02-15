# 415. 字符串相加
# 难度 简单
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
# 
# 示例 1：
# 输入：num1 = "11", num2 = "123"
# 输出："134"
# 
# 示例 2：
# 输入：num1 = "456", num2 = "77"
# 输出："533"
# 
# 示例 3：
# 输入：num1 = "0", num2 = "0"
# 输出："0"

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        up = 0
        while i >= 0 and j >= 0:
            r = int(num1[i]) + int(num2[j]) + up
            i -= 1
            j -= 1
            up = 0
            if r > 9:
                r = r - 10
                up = 1
            res.append(r)
        while i >= 0:
            r = int(num1[i]) + up
            i -= 1
            up = 0
            if r > 9:
                r = r - 10
                up = 1
            res.append(r)
        while j >= 0:
            r = int(num2[j]) + up
            j -= 1
            up = 0
            if r > 9:
                r = r - 10
                up = 1
            res.append(r)
        if up > 0:
            res.append(up)
        res.reverse()
        return ''.join([str(s) for s in res])

if __name__ == '__main__':
    num1 = "456"
    num2 = "77"
    print(Solution().addStrings(num1, num2))