/**
287. 寻找重复数
难度 中等
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3

提示：
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次

进阶：
如何证明 nums 中至少存在一个重复的数字?
你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
*/

/**
二分查找发。
如果是 [1, n] 的数字组成长度为 n 的数组，并且没有重复，显然 1-n 各出现了一次。
整个数组中，一共有 1 个数字 <= 1, 2 个数字 <= 2, ..., n 个数字 <= n。
此时再往里面添加一个 [1, n] 之间的数字，假如是 x，则
一共有 1 个数字 <= 1, 2个数字 <= 2, ..., x+1 个数字 小于等于 x, ... x+1+1 个数字小于等于 x+1, n+1 个数字 <= n。
所以可以使用二分法来逐渐猜出 x 是谁。
*/

package main

func findDuplicate(nums []int) int {
	length := len(nums)
	left, right := 1, length-1
	for left < right {
		mid := left + (right-left)/2
		// cnt 记录有多少个数字 <= num
		cnt := 0
		for i := 0; i < length; i++ {
			if nums[i] <= mid {
				cnt++
			}
		}
		if cnt <= mid {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}
