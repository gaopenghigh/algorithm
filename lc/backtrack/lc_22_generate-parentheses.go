/**
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
*/

/**
题目可以变形为，在 2n 的位置上，从 n 个 '(' 和 n 个 ')' 中选择符号进行放置，找到所有的合法组合。
通过的方法判断是否合法：
在任一一个位置 i，考察它前面的部分， '(' 的个数一定 >= ')' 的个数；
回溯算法中，“选择”就是针对每个位置，选择 ( 或者选择 )，”可选列表“就是剩下的 ( 和 )
*/

package main

import (
	"fmt"
	"strings"
)

func generateParenthesis(n int) []string {
	left := n
	right := n
	track := []string{}
	res := []string{}
	backtrack(n, &res, &track, left, right)
	return res
}

// left 和 right 表示当前还能选的 ( 数和 ) 数
func backtrack(n int, res *[]string, track *[]string, left, right int) {
	if left == right && left == 0 {
		s := strings.Join(*track, "")
		*res = append(*res, s)
		return
	}
	if left < 0 || right < 0 {
		return
	}
	// 当前选择不对，因为剩下的 '(' 一定要小于等于剩下的 ')'
	if left > right {
		return
	}
	// 选择 '('
	*track = append(*track, "(")
	backtrack(n, res, track, left-1, right)
	*track = (*track)[:len(*track)-1]
	// 选择 ')'
	*track = append(*track, ")")
	backtrack(n, res, track, left, right-1)
	*track = (*track)[:len(*track)-1]
}

func main() {
	fmt.Println(generateParenthesis(3))
}
