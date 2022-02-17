/**
79. 单词搜索
难度 中等
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [["A","B","C","E"],
              ["S","F","C","S"],
			  ["A","D","E","E"]],
     word = "ABCCED"
输出：true

示例 2：
输入：board = [["A","B","C","E"],
              ["S","F","C","S"],
			  ["A","D","E","E"]],
	 word = "SEE"
输出：true

示例 3：
输入：board = [["A","B","C","E"],
			  ["S","F","C","S"],
			  ["A","D","E","E"]],
	 word = "ABCB"
输出：false
*/

/**
回溯，主要是需要定义好回溯的方法。
backtrack(i, j, k) 返回从 board[i][j] 开始，能否找到单词 word[k:]
*/

package main

func exist(board [][]byte, word string) bool {
	visited := [][]bool{}
	for _, row := range board {
		visitedRow := []bool{}
		for _ = range row {
			visitedRow = append(visitedRow, false)
		}
		visited = append(visited, visitedRow)
	}

	for i, row := range board {
		for j := range row {
			if backtrack(visited, board, i, j, 0, word) {
				return true
			}
		}
	}
	return false
}

func backtrack(visited [][]bool, board [][]byte, i, j, k int, word string) bool {
	if board[i][j] != word[k] {
		return false
	}

	if k == len(word)-1 {
		return true
	}

	rows := len(board)
	cols := len(board[0])

	visited[i][j] = true
	// up, down, left, right
	directions := [][]int{{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}}
	for _, direction := range directions {
		x, y := direction[0], direction[1]
		if 0 <= x && x < rows && 0 <= y && y < cols {
			if visited[x][y] {
				continue
			}
			if backtrack(visited, board, x, y, k+1, word) {
				return true
			}
		}
	}
	visited[i][j] = false
	return false
}
