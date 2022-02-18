/**
238. 除自身以外数组的乘积
难度 中等
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请不要使用除法，且在 O(n) 时间复杂度内完成此题。

示例 1:
输入: nums = [1,2,3,4]
输出: [24,12,8,6]

示例 2:
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
*/

/**
通过 2 次遍历，分别求出每个位置左边所有元素的乘积以及右边所有元素的乘积
*/

package main

func productExceptSelf(nums []int) []int {
	left := make([]int, len(nums))
	right := make([]int, len(nums))
	left[0] = 1
	right[len(nums)-1] = 1
	i := 1
	for i < len(nums) {
		left[i] = nums[i-1] * left[i-1]
		i++
	}
	i = len(nums) - 2
	for i >= 0 {
		right[i] = nums[i+1] * right[i+1]
		i--
	}
	res := make([]int, len(nums))
	i = 0
	for i < len(nums) {
		res[i] = left[i] * right[i]
		i++
	}
	return res
}
