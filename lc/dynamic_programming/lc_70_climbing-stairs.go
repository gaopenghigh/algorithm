/**
70. 爬楼梯
难度 简单
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
*/

/**
可以拆分为子问题，通过子问题的解得到最终的解，考虑 DP。
dp(i) 表示走到第 i 阶的方法数，则 dp(i) = dp(i-1) + dp(i-2)
base case
dp(1) = 1
dp(2) = 2
*/

package main

import "fmt"

var memo = map[int]int{}

func climbStairs(n int) int {
	switch n {
	case 0:
		return 0
	case 1:
		return 1
	case 2:
		return 2
	}
	if v, ok := memo[n]; ok {
		return v
	}
	r := climbStairs(n-1) + climbStairs(n-2)
	memo[n] = r
	return r
}

func main() {
	fmt.Println(climbStairs(3))
}
