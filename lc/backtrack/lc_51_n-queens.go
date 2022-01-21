/*
51. N 皇后
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]
*/
package main

import (
	"fmt"
)

func solveNQueens(n int) [][]string {
	board := make([][]string, n)
	for row := range board {
		board[row] = make([]string, n)
	}
	for row := range board {
		for col := range board[row] {
			board[row][col] = "."
		}
	}

	// board[1][1] = "Q"
	// fmt.Println(copyBoard(board))
	// fmt.Println(isValid(board, 2, 0))

	res := [][][]string{}
	backtrack(&res, board, 0)

	// fmt.Println("got", len(res), "answers")
	// 将 [][]string 转换为 []string 的形式
	answers := make([][]string, 0)
	for b := range res {
		ans := make([]string, n)
		for row := range res[b] {
			rowLine := ""
			for col := range res[b][row] {
				rowLine += res[b][row][col]
			}
			ans[row] = rowLine
		}
		answers = append(answers, ans)
	}
	// fmt.Println("got", len(answers), "answers")
	return answers
}

func backtrack(res *[][][]string, board [][]string, row int) {
	// fmt.Printf("res = %v board = %v , row=%v\n", res, board, row)
	n := len(board)
	if row == n {
		*res = append(*res, copyBoard(board))
		return
	}

	for col := 0; col < n; col++ {
		if !isValid(board, row, col) {
			continue
		}
		board[row][col] = "Q"
		backtrack(res, board, row+1)
		board[row][col] = "."
	}
}

func copyBoard(board [][]string) [][]string {
	n := len(board)
	r := make([][]string, n)
	for row := range board {
		r[row] = make([]string, n)
		copy(r[row], board[row])
	}
	return r
}

func isValid(board [][]string, row, col int) bool {
	n := len(board)
	// 检查同一列是否有冲突
	for i := 0; i < n; i++ {
		if i != row && board[i][col] == "Q" {
			return false
		}
	}
	// 检查左上方是否有冲突
	for i, j := row-1, col-1; i >= 0 && j >= 0; i, j = i-1, j-1 {
		if board[i][j] == "Q" {
			return false
		}
	}
	// 检查右上方是否有冲突
	for i, j := row-1, col+1; i >= 0 && j < n; i, j = i-1, j+1 {
		if board[i][j] == "Q" {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(solveNQueens((4)))
}
