/**
406. 根据身高重建队列
难度 中等
假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。
每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，
其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。

示例 1：
输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
解释：
编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。

示例 2：
输入：people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
输出：[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

提示：
1 <= people.length <= 2000
0 <= hi <= 106
0 <= ki < people.length
题目数据确保队列可以被重建
*/

/**
题目需要返回的就是这个队到底是怎么排的。
这类问题有个套路：一般这种数对，还涉及排序的，根据第一个元素正向排序， 根据第二个元素反向排序，
或者根据第一个元素反向排序，根据第二个元素正向排序，往往能够简化解题过程。

下面参考链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/406-gen-ju-shen-gao-zhong-jian-dui-lie-x-a4w7/
我们先按照身高从大到小排序（身高相同的情况下K小的在前面），这样的话，无论哪个人的身高都小于等于他前面人的身高。
所以接下来只要按照K值将他插入相应的位置就可以了。
因为前面的每个人身高都比它大， 但是他前面只能有 K 个人大于等于它的身高，所以他只能放在第K个位置。
例如：示例1排完序：[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]

新建一个二维vector：
[7,0]插入第0的位置
[7,1]插入第1的位置
[6,1]插入第1的位置，这时[7,1]就往后移一位了
........
*/

package main

import "sort"

type Peoples [][]int

func (p Peoples) Len() int {
	return len(p)
}

// 从大到小排序，身高一样的话 k 值较小的放在前面
func (p Peoples) Less(i, j int) bool {
	if p[i][0] > p[j][0] {
		return true
	}
	if p[i][0] == p[j][0] {
		if p[i][1] < p[j][1] {
			return true
		}
	}
	return false
}

func (p Peoples) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func reconstructQueue(people [][]int) [][]int {
	var peoples Peoples
	peoples = people
	sort.Sort(peoples)

	res := [][]int{}
	for _, p := range peoples {
		peopleBefore := p[1]
		if len(res) <= peopleBefore {
			res = append(res, p)
		} else { // 插入
			right := append([][]int{p}, res[peopleBefore:]...)
			res = append(res[:peopleBefore], right...)
		}
	}
	return res
}
