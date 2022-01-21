/**
77. 组合
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。
*/
package main

import "fmt"

func combine(n int, k int) [][]int {
	res := [][]int{}
	track := []int{}
	used := make(map[int]bool, n)
	for i := 1; i <= n; i++ {
		used[i] = false
	}
	backtrack(n, k, &res, &track, 1)
	return res
}

func backtrack(n, k int, res *[][]int, track *[]int, start int) {
	if len(*track) == k {
		*res = append(*res, copySlice(*track))
		return
	}

	for i := start; i <= n; i++ {
		*track = append(*track, i)
		backtrack(n, k, res, track, i+1)
		*track = (*track)[:len(*track)-1]
	}
}

func copySlice(s []int) []int {
	t := make([]int, len(s))
	copy(t, s)
	return t
}

func main() {
	fmt.Println(combine(3, 3))
}
