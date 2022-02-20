/**
448. 找到所有数组中消失的数字
难度 简单
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

示例 1：
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]

示例 2：
输入：nums = [1,1]
输出：[2]
*/

// 技巧就是利用 index 做标记
func findDisappearedNumbers(nums []int) []int {
	for _, num := range nums {
		if num < 0 {
			num = num * -1
		}
		if nums[num-1] > 0 {
			nums[num-1] = nums[num-1] * -1
		}
	}
	res := []int{}
	i := 1
	for i <= len(nums) {
		if nums[i-1] > 0 {
			res = append(res, i)
		}
		i++
	}
	return res
}