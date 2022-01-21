/**
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
*/

package main

import (
	"fmt"
)

/**
回溯遍历，并且回溯中的所有路径都可以加入到最终的结果中
*/

func subsets(nums []int) [][]int {
	res := [][]int{}
	track := []int{}
	backtrack(nums, &res, &track, 0)
	return res
}

func backtrack(nums []int, res *[][]int, track *[]int, start int) {
	*res = append(*res, copySlice(*track))
	for i := start; i < len(nums); i++ {
		*track = append(*track, nums[i])
		backtrack(nums, res, track, i+1)
		*track = (*track)[:len(*track)-1]
	}
}

func copySlice(s []int) []int {
	t := make([]int, len(s))
	copy(t, s)
	return t
}

func main() {
	nums := []int{1, 2, 3}
	fmt.Println(subsets(nums))
}
