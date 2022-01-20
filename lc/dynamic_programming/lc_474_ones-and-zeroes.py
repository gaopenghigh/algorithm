# 474. 一和零
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
# 
# 示例 1：
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
# 
# 示例 2：
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
# 
# 提示：
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] 仅由 '0' 和 '1' 组成
# 1 <= m, n <= 100


# dp[i][j][k] 中 i, j 和 k 描述状态，从前 i 个元素中选择满足要求的最大子集，其中最多有 j 个 0 和 k 个 1
# i 的最大值为 len(strs), j 和 k 的最大值为 m 和 n
# base case: dp[0][x][x] = 0
# 假设 strs[i] 有 x 个 '0' 和 y 个 '1'
# 如果最终的最大子集中包含了 strs[i]，则 dp[i][j][k] = 1 + dp[i-1][j-x][k-y]
# 如果最大子集中不包含 strs[i]，则 dp[i][j][k] = dp[i-1][j][k]
# 取其中的最大值作为 dp[i][j][k] 的值
# 最终的答案就是 dp[len(strs)][m][n]

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [
                [
                    [ 0 for _ in range(n + 1) ] for _ in range(m + 1)
                ] for _ in range(len(strs) + 1)
            ]
        for i in range(1, len(strs)+1):
            s = strs[i-1]
            n0 = len([i for i in s if i == '0'])
            n1 = len(s) - n0
            for j in range(m+1):
                for k in range(n+1):
                    if j >= n0 and k >= n1:
                        dp[i][j][k] = max(
                            1 + dp[i-1][j-n0][k-n1],  # 选择
                            dp[i-1][j][k] # 不选择
                        )
                    else: # 只能不选择
                        dp[i][j][k] = dp[i-1][j][k] # 不选择
        return dp[len(strs)][m][n]

if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(Solution().findMaxForm(strs, m, n))