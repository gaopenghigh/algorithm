# 91. 解码方法
# 难度 中等
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
# 题目数据保证答案肯定是一个 32 位 的整数。
# 
# 示例 1：
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 示例 2：
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 示例 3：
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
# 
# 提示：
# 1 <= s.length <= 100
# s 只包含数字，并且可能包含前导零。


# 动态规划第一步要明确两点，「状态」和「选择」。
# 状态，就是对一个局面的描述。通过一个状态，可以定义一个子问题，而动态规划的核心就是分解为子问题。
# 选择，就是某个动作，通过一个动作，问题可以拆解为子问题
# 动态规划的框架如下：
# for 状态1 in 状态1的所有取值：
#     for 状态2 in 状态2的所有取值：
#         for ...
#             dp[状态1][状态2][...] = 择优(选择1，选择2...)
#
# 本题中，“状态”就是带解码的字符串，
# 至于选择，对于每个字符串的最后一个字符，可以选择自成一体，或者选择与它前面的字符合体。
# 使用 dp[i] = x 表示 s[:i] 最多有 x 中解码方式。
# 对于 s[:i] 的最后一个字符 s[i-1]，有如下几种情况
# 1. s[i-1] 自称一体，前提是 1 <= int(s[i-1]) <= 9，则 dp[i] = dp[i-1]
# 2. s[i-1] 和 s[i-2] 合体，前提是 s[i-2] != '0' 并且 1 <= int(s[i-2]) * 10 + int(s[i-1]) <= 26，则 dp[i] = dp[i-2]
# 两者之和就是最终 dp[i] 的值
# base case: dp[0] = 1, 表示空字符串也算是一种解码方法
# 另外由于 dp[i] 只依赖于 dp[i-1] 和 dp[i-2]，所以可以压缩 dp 数组，只用 3 个变量即可

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            x = 0
            if 1 <= int(s[i-1]) <= 9:
                x = dp[i-1]
            if s[i-2] != '0' and 1 <= int(s[i-2])*10 + int(s[i-1]) <= 26:
                x += dp[i-2]
            dp[i] = x
        return dp[len(s)]

if __name__ == '__main__':
    s = '12'
    print(Solution().numDecodings(s))