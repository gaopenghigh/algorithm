/**
169. 多数元素
难度 简单
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：[3,2,3]
输出：3

示例 2：
输入：[2,2,1,1,1,2,2]
输出：2

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
*/

/**
最直观的方法就是哈希表。
也可以先排序然后找中间位置的数。
要做到空间复杂度 O(1) 需要使用 Boyer-Moore 投票算法，比较技巧性。
*/
package main

import "fmt"

// 使用排序的方法
func majorityElement(nums []int) int {
	quickSort(nums, 0, len(nums)-1)
	return nums[len(nums)/2]
}

func quickSort(nums []int, low, high int) {
	if low >= high {
		return
	}
	pivot := nums[low]
	slow := low
	fast := low + 1
	for fast <= high {
		// fmt.Printf("low=%d, high=%d, slow=%d, fast=%d, pivot=%d, nums[fast]=%d, nums=%v\n", low, high, slow, fast, pivot, nums[fast], nums)
		if nums[fast] <= pivot {
			slow++
			nums[slow], nums[fast] = nums[fast], nums[slow]
		}
		fast++
	}
	nums[low], nums[slow] = nums[slow], nums[low]
	quickSort(nums, low, slow-1)
	quickSort(nums, slow+1, high)
}

func main() {
	nums := []int{3, 2, 3}
	quickSort(nums, 0, len(nums)-1)
	fmt.Println(nums)
}
