# 8. 字符串转换整数 (atoi)
# 难度 中等
# 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
# 函数 myAtoi(string s) 的算法如下：
# 读入字符串并丢弃无用的前导空格
# 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
# 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
# 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
# 如果整数数超过 32 位有符号整数范围 [−2^31,  2^31 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −2^31 的整数应该被固定为 −2^31 ，大于 2^31 − 1 的整数应该被固定为 2^31 − 1 。
# 返回整数作为最终结果。
# 注意：
# 本题中的空白字符只包括空格字符 ' ' 。
# 除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
# 
# 示例 1：
# 输入：s = "42"
# 输出：42
# 解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
# 第 1 步："42"（当前没有读入字符，因为没有前导空格）
# 第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
# 第 3 步："42"（读入 "42"）
# 解析得到整数 42 。
# 由于 "42" 在范围 [-2^31, 2^31 - 1] 内，最终结果为 42 。
# 
# 示例 2：
# 输入：s = "   -42"
# 输出：-42
# 解释：
# 第 1 步："   -42"（读入前导空格，但忽视掉）
# 第 2 步："   -42"（读入 '-' 字符，所以结果应该是负数）
# 第 3 步："   -42"（读入 "42"）
# 解析得到整数 -42 。
# 由于 "-42" 在范围 [-2^31, 2^31 - 1] 内，最终结果为 -42 。


NUM_MAX = 2**31-1
NUM_MIN = -2**31

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s):
            return 0

        op = 1
        if s[i] == "-":
            op = -1
            i += 1
        elif s[i] == "+":
            i += 1
        
        n = 0
        while i <len(s):
            if not s[i].isnumeric():
                break
            n = n*10 + int(s[i])
            if op * n > NUM_MAX:
                return NUM_MAX
            if op * n < NUM_MIN:
                return NUM_MIN
            i += 1
        return op * n

if __name__ == '__main__':
    print(Solution().myAtoi(" 32 aaa "))
