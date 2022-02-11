/**
752. 打开转盘锁
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。

示例 1:
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。

示例 2:
输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。
*/

package main

import (
	"container/list"
	"fmt"
	"strconv"
)

/**
使用 BFS 的思想，拨一步能走到哪些情况，拨 2 步能走到哪些情况等等。
一共有 4 个位置，每个位置可以向上拨或者向下拨，所以一共 8 种情况，相当于每个节点有 8 个 顶点与它连接。
*/

func openLock(deadends []string, target string) int {
	deadendsMap := make(map[string]bool)
	for _, s := range deadends {
		deadendsMap[s] = true
	}
	if _, found := deadendsMap["0000"]; found {
		return -1
	}

	visited := make(map[string]bool)
	visited["0000"] = true
	q := list.New()
	q.PushBack("0000")
	steps := 0
	for q.Len() > 0 {
		size := q.Len()
		// fmt.Println("size=", size)
		for i := 0; i < size; i++ {
			e := q.Front()
			q.Remove(e)
			s := e.Value.(string)
			visited[s] = true
			if s == target {
				return steps
			}
			for _, adj := range next(s) {
				if _, found := deadendsMap[adj]; found {
					continue
				}
				if _, found := visited[adj]; found {
					continue
				}
				q.PushBack(adj)
				visited[adj] = true
			}
		}
		steps++
	}

	return -1
}

// 4 个位置中的任意一个拨动一步可能变成的数字，应该有 8 个
func next(s string) []string {
	res := []string{}
	res = append(res, up(s)...)
	res = append(res, down(s)...)
	return res
}

// 往上拨，0 -> 1,  2->2, ..., 9->0
func up(s string) []string {
	res := []string{}
	for i, c := range s {
		num, err := strconv.Atoi(string(c))
		if err != nil {
			panic(err)
		}
		nextNum := num + 1
		if num == 9 {
			nextNum = 0
		}
		nextStr := s[:i] + strconv.Itoa(nextNum) + s[i+1:]
		res = append(res, nextStr)
	}
	return res
}

// 往下拨，9->8, 8->7, ..., 0->9
func down(s string) []string {
	res := []string{}
	for i, c := range s {
		num, err := strconv.Atoi(string(c))
		if err != nil {
			panic(err)
		}
		nextNum := num - 1
		if num == 0 {
			nextNum = 9
		}
		nextStr := s[:i] + strconv.Itoa(nextNum) + s[i+1:]
		res = append(res, nextStr)
	}
	return res
}

func main() {
	/*
		deadends := []string{"0009"}
		target := "0009"
	*/
	deadends := []string{"0201", "0101", "0102", "1212", "2002"}
	target := "0202"
	fmt.Println(openLock(deadends, target))
}
