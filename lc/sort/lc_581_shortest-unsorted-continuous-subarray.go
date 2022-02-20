/**
581. 最短无序连续子数组
难度 中等
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。

示例 1：
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

示例 2：
输入：nums = [1,2,3,4]
输出：0

示例 3：
输入：nums = [1]
输出：0
*/

/**
思路与算法
我们将给定的数组 nums 表示为三段子数组拼接的形式，分别记作
numsA， numsB， numsC。当我们对 numsB 进行排序，整个数组将变为有序。
换而言之，当我们对整个序列进行排序， numsA 和 numsC 都不会改变。
本题要求我们找到最短的 numsB ​，即找到最大的
numsA 和 numsC 的长度之和。因此我们将原数组
nums 排序与原数组进行比较，取最长的相同的前缀为
numsA，取最长的相同的后缀为 numsC，这样我们就可以取到最短的
numsB​。
*/
package main

import (
	"sort"
)

func findUnsortedSubarray(nums []int) int {
	sortedNums := make([]int, len(nums))
	copy(sortedNums, nums)
	sort.Ints(sortedNums)
	left := 0
	for left < len(sortedNums) {
		if nums[left] == sortedNums[left] {
			left++
		} else {
			break
		}
	}
	right := len(sortedNums) - 1
	for right >= 0 {
		if nums[right] == sortedNums[right] {
			right--
		} else {
			break
		}
	}
	if left >= right {
		return 0
	}
	return right - left + 1
}
