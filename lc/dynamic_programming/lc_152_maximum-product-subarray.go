/**
152. 乘积最大子数组
难度 中等
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
测试用例的答案是一个 32-位 整数。
子数组 是数组的连续子序列。

示例 1:
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
*/

/**
求最值，考虑用 DP。
题是求数组中子区间的最大乘积，对于乘法，我们需要注意，负数乘以负数，会变成正数，所以解这题的时候我们需要维护两个变量，当前的最大值，以及最小值，最小值可能为负数，但没准下一步乘以一个负数，当前的最大值就变成最小值，而最小值则变成最大值了。

设
maxDp(i) 表示以 nums[i] 结尾的乘积最大的非空连续子数组的值，
minDp(i) 表示以 nums[i] 结尾的乘积最小的非空连续子数组的值，可能为负数
则：
如果 nums[i] > 0, 则 maxDp(i) = max(maxDp(i-1)*nums[i], nums[i]), minDp(i) = min(minDp(i-1)*nums[i], nums[i])
如果 nums[i] < 0, 则 maxDp(i) = max(minDp(i-1)*nums[i], nums[i]), minDp(i) = min(maxDp(i-1)*nums[i], nums[i])
如果 nums[i] == 0, 则 maxDp(i) = 0, minDp(i) = 0
合起来就是：
maxDp(i) = max(
	max(maxDp(i-1)*nums[i], nums[i]),
	max(minDp(i-1)*nums[i], nums[i])
)
minDp(i) = min(
	min(minDp(i-1)*nums[i], nums[i]),
	min(maxDp(i-1)*nums[i], nums[i])
)

Base Case
maxDp(0) = minDp(0) = nums[0]
*/

package main

func maxProduct(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	maxDp := make([]int, len(nums))
	minDp := make([]int, len(nums))
	maxDp[0] = nums[0]
	minDp[0] = nums[0]

	i := 1
	for i < len(nums) {
		num := nums[i]
		maxDp[i] = max(
			max(maxDp[i-1]*num, num),
			max(minDp[i-1]*num, num),
		)
		minDp[i] = min(
			min(minDp[i-1]*num, num),
			min(maxDp[i-1]*num, num),
		)
		i++
	}

	r := maxDp[0]
	for _, v := range maxDp {
		if v > r {
			r = v
		}
	}
	return r
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x > y {
		return y
	}
	return x
}
