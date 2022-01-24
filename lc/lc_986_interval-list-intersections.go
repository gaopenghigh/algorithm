/**
986. 区间列表的交集
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。
返回这 两个区间列表的交集 。
形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。
两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

示例 1：
输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

示例 2：
输入：firstList = [[1,3],[5,9]], secondList = []
输出：[]
*/

/**
使用双指针
*/
package main

func intervalIntersection(firstList [][]int, secondList [][]int) [][]int {
	res := [][]int{}
	i, j := 0, 0
	for i < len(firstList) && j < len(secondList) {
		startI, endI := firstList[i][0], firstList[i][1]
		startJ, endJ := secondList[j][0], secondList[j][1]
		// 如果有交集，则 start 是较大的那个，end 是较小的那个
		start := max(startI, startJ)
		end := min(endI, endJ)
		if start <= end {
			res = append(res, []int{start, end})
		}
		if endI < endJ {
			i++
		} else {
			j++
		}
	}
	return res
}

func min(i, j int) int {
	if i < j {
		return i
	}
	return j
}

func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}
