/**
75. 颜色分类
难度 中等
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库的sort函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]
*/

/**
直接 sort 或者使用双指针法，将 0 移动到左边，2 移动到右边
*/

package main

func sortColors(nums []int) {
	// put all 0 to left side
	slow := -1
	fast := 0
	for fast < len(nums) {
		if nums[fast] == 0 {
			slow++
			nums[slow], nums[fast] = nums[fast], nums[slow]
		}
		fast++
	}
	// put all 2 to right side
	slow = len(nums)
	fast = len(nums) - 1
	for fast >= 0 {
		if nums[fast] == 2 {
			slow--
			nums[slow], nums[fast] = nums[fast], nums[slow]
		}
		fast--
	}
}
