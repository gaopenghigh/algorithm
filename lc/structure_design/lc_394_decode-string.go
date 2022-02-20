/**
394. 字符串解码
难度 中等
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

提示：
1 <= s.length <= 30
s 由小写英文字母、数字和方括号 '[]' 组成
s 保证是一个 有效 的输入。
s 中所有整数的取值范围为 [1, 300]
*/

/**
通用的解法是使用栈，但需要处理的细节比较多。
仔细分析一下题目，也可以使用递归，细节会少一些。
*/

package main

import (
	"fmt"
	"strconv"
	"strings"
)

// 使用栈
func decodeString2(s string) string {
	stk := NewStack()
	for _, b := range s {
		c := string(b)
		if c != "]" {
			stk.Push(c)
			continue
		}
		subStr := getStr(stk)
		stk.Push(subStr)
	}
	return strings.Join(stk.Datas, "")
}

func getStr(stk *Stack) string {
	r := ""
	for {
		c := stk.Pop()
		if c != "[" {
			r = c + r
		} else {
			n := getNum(stk)
			multiple := ""
			for n >= 1 {
				multiple = multiple + r
				n--
			}
			return multiple
		}
	}
}

func getNum(stk *Stack) int {
	numStr := ""
	for stk.Len() > 0 {
		c := stk.Top()
		if _, err := strconv.Atoi(c); err == nil {
			numStr = c + numStr
			stk.Pop()
		} else {
			break
		}
	}
	n, err := strconv.Atoi(numStr)
	if err != nil {
		panic(err)
	}
	return n
}

type Stack struct {
	Datas []string
}

func NewStack() *Stack {
	return &Stack{
		Datas: []string{},
	}
}

func (s *Stack) Push(e string) {
	s.Datas = append(s.Datas, e)
}

func (s *Stack) Pop() string {
	r := s.Datas[len(s.Datas)-1]
	s.Datas = s.Datas[0 : len(s.Datas)-1]
	return r
}

func (s *Stack) Top() string {
	return s.Datas[len(s.Datas)-1]
}

func (s *Stack) Len() int {
	return len(s.Datas)
}

// 使用递归
func decodeString(s string) string {
	_, r := decode(0, s)
	return r
}

func decode(idx int, s string) (int, string) {
	res := []string{}
	num := 0
	for idx < len(s) {
		c := string(s[idx])
		if n, err := strconv.Atoi(c); err == nil {
			num = num*10 + n
		} else if c == "[" {
			i, subStr := decode(idx+1, s)
			for num > 0 {
				res = append(res, subStr)
				num--
			}
			num = 0
			idx = i
		} else if c == "]" {
			return idx, strings.Join(res, "")
		} else {
			res = append(res, c)
		}
		idx++
	}
	return idx, strings.Join(res, "")
}

func main() {
	s := "1[a]2[b2[c]]"
	fmt.Println(decodeString(s))
}
