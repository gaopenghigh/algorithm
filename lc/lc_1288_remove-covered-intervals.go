/**
1288. 删除被覆盖区间
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。
在完成所有删除操作后，请你返回列表中剩余区间的数目。
示例：
输入：intervals = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。

提示：​​​​​​
1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
对于所有的 i != j：intervals[i] != intervals[j]
*/

/**
区间或者线段问题，一个通用的技巧是按照每个线段的起始位置 start 的升序排序，相同 start 的，再按照结尾位置 end 的降序排序，这样只要 start 一样，上面的区间一定覆盖下面的区间。
排序后，如果上面的区间覆盖下面一个区间，则下面区间的 end 一定小于等于上区间的 end。反过来说，如果一个区间不被任何区间覆盖，则它的 end 一定大于它上面没有被覆盖掉的那个个区间的 end。

-------
------
------
---
  ----
  --
    ------
     -------
     ---
**/

package main

import (
	"sort"
)

type Intervals [][]int

func (intervals Intervals) Len() int {
	return len(intervals)
}

func (intervals Intervals) Less(i, j int) bool {
	if intervals[i][0] < intervals[j][0] {
		return true
	}
	if intervals[i][0] == intervals[j][0] {
		if intervals[i][1] > intervals[j][1] {
			return true
		}
	}
	return false
}

func (intervals Intervals) Swap(i, j int) {
	intervals[i], intervals[j] = intervals[j], intervals[i]
}

func removeCoveredIntervals(intervals [][]int) int {
	res := 1
	sortedIntervals := Intervals(intervals)
	sort.Sort(sortedIntervals)
	preEnd := sortedIntervals[0][1]
	for i := 1; i < len(sortedIntervals); i++ {
		interval := sortedIntervals[i]
		end := interval[1]
		// 否则就被覆盖掉了
		if end > preEnd {
			res++
			preEnd = end
		}
	}
	return res
}
