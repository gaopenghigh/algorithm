# 7. 整数反转
# 难度 中等
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
# 示例 1：
# 输入：x = 123
# 输出：321
# 
# 示例 2：
# 输入：x = -123
# 输出：-321
# 
# 示例 3：
# 输入：x = 120
# 输出：21
# 
# 示例 4：
# 输入：x = 0
# 输出：0


class Solution:
    # 转换成字符串处理
    def reverse(self, x: int) -> int:
        s = str(x)
        op = 1
        if s.startswith('-'):
            s = s[1:]
            op = -1
        r = op * int(s[::-1])
        if r < -2**31 or r > 2**31 - 1:
            return 0
        return r

    # 完全用数字处理
    def reverse2(self, x: int) -> int:
        N_MAX = 2**31 -1
        N_MIN = -2**31
        op = 1 if x >= 0 else -1
        if x < 0:
            x = -1*x
        r = 0
        while x != 0:
            n = x % 10
            r = r*10 + n
            # print(f'x={x}, r={r}, n={n}')
            if r*op < N_MIN or r*op > N_MAX: 
                return 0
            x = x // 10
        return r*op

if __name__ == '__main__':
    print(Solution().reverse2(-1234))
