/*
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
*/

/*
标准回溯算法，回溯算法框架：
result = []
def backtrack(路径，选择列表)：
    if 满足结束条件:
        result.append(路径)
        return
    for 选择 in 选择列表：
        将选择加入路径
        backtrack（路径，新的选择列表）   # 新的选择列表可能和老的一样，也有可能不一样
        将选择从路径中移除
*/

package main

import (
	"fmt"
)

var (
	res  [][]int
	used map[int]bool
)

func permute(nums []int) [][]int {
	res = [][]int{}
	used = make(map[int]bool, len(nums))
	for _, n := range nums {
		used[n] = false
	}
	backtrack([]int{}, nums)
	return res
}

func backtrack(path []int, nums []int) {
	if len(path) == len(nums) {
		tmp := make([]int, len(path))
		copy(tmp, path)
		res = append(res, tmp)
		return
	}
	for _, n := range nums {
		if !used[n] {
			path = append(path, n)
			used[n] = true
			backtrack(path, nums)
			path = path[:len(path)-1]
			used[n] = false
		}
	}
}

func main() {
	nums := []int{1, 2, 3, 4}
	fmt.Println(permute(nums))
}
