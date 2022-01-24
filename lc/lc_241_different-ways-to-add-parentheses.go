/**
241. 为运算表达式设计优先级
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
示例 1:

输入: "2-1-1"
输出: [0, 2]
解释:
((2-1)-1) = 0
(2-(1-1)) = 2

示例 2:
输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
*/

/**
注意：题中有一个隐藏的意思。通过加括号之后，所有运算的优先级都一样了，比如 2*(3-4)*5 这种看起来合理，但实际上应该写成 (2*(3-4))*5 ，也就是每两个元素和一个符号，就需要加一个括号。
如果只有 2 个数字，x op y，则只能整个加括号： (x op1 y)
如果有 3 个数字，x op1 y op2 z ，则可能为 ((x op1 y) op2 z) 或 (x op1 (y op2 z))
也就是可以通过递归的方式，分解为两部分 A op1 B，A 为 x , B 为 y op2 z ，
或者 A op2 B，A 为 x op1 y , B 为 z

所以对于一个表达式，可以再任意符号的位置分层左右两部分，分别针对左边的所有情况，使用该符号所代表的计算方式，匹配右边的所有情况。
*/

package main

import (
	"fmt"
	"strconv"
)

func diffWaysToCompute(expression string) []int {
	res := []int{}
	for i, b := range expression {
		c := string(b)
		if c == "+" || c == "-" || c == "*" {
			left := diffWaysToCompute(expression[:i])
			right := diffWaysToCompute(expression[i+1:])
			for _, l := range left {
				for _, r := range right {
					if c == "+" {
						res = append(res, l+r)
					} else if c == "-" {
						res = append(res, l-r)
					} else if c == "*" {
						res = append(res, l*r)
					} else {
						panic(c)
					}
				}
			}
		}
	}
	// 不包含运算符号，是一个数字
	if len(res) == 0 {
		n, err := strconv.Atoi(expression)
		if err != nil {
			panic(err)
		}
		res = append(res, n)
	}
	return res
}

func main() {
	s := "2*3-4*5"
	fmt.Println(diffWaysToCompute((s)))
}
