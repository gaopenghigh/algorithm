/**
56. 合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
*/

/**
和 1288 类似。按照 start 升序排序，
对于中间的任意一个区间，如果它的 start 小于等于上一个区间的 end，则可以被合并掉，合并后的区间 end 为之前两个区间中较长的一个。
*/

package main

import "sort"

type Intervals [][]int

func (intervals Intervals) Len() int {
	return len(intervals)
}

func (intervals Intervals) Less(i, j int) bool {
	return intervals[i][0] < intervals[j][0]
}

func (intervals Intervals) Swap(i, j int) {
	intervals[i], intervals[j] = intervals[j], intervals[i]
}

func merge(intervals [][]int) [][]int {
	res := [][]int{}
	sortedIntervals := Intervals(intervals)
	sort.Sort(sortedIntervals)

	preStart := sortedIntervals[0][0]
	preEnd := sortedIntervals[0][1]
	for i := 1; i < sortedIntervals.Len(); i++ {
		interval := sortedIntervals[i]
		start := interval[0]
		end := interval[1]
		if start <= preEnd {
			if end > preEnd {
				preEnd = end
			}
			continue
		}
		// 新的区间
		res = append(res, []int{preStart, preEnd})
		preStart = start
		preEnd = end
	}
	// 最后可能剩下没有重叠的部分
	res = append(res, []int{preStart, preEnd})
	return res
}
