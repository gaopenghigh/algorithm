/**
279. 完全平方数
难度 中等
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9
*/

/**
n = x*x + y*y + z*z + ...
也可以写成 n = j*j + k
也就是如果我们知道和为 k 的完全平方数的最少数量，则和为 n 的完全平方数的最少数量就是再加上 1.
也就是可以为同样性质的子问题，考虑动态规划。
驾驶 dp[i] 表示和为 i 的完全平方数的最少数量，则
dp[i] = 1 + min(dp[i - j*j]) for j in [1, sqr(i)]
Base Case
dp[1] = 1
*/

package main

func numSquares(n int) int {
	dp := make([]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = i
	}
	for i := 2; i <= n; i++ {
		for j := 1; j*j <= i; j++ {
			dp[i] = min(dp[i], 1+dp[i-j*j])
		}
	}
	return dp[n]
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
