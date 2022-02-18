/**
128. 最长连续序列
难度 中等
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
*/

/**
使用一个 map 存出现过的字符。然后逐个看 map 中的字符，假如是 n，
如果 n - 1 不在 map 中，那 n 可能是最长连续序列的开始，则
依次找 n+1, n+2, ... 知道找不到为止，记录最长的长度
*/

package main

func longestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	lcs := 0
	m := make(map[int]bool, len(nums))
	for _, n := range nums {
		m[n] = true
	}

	for n, _ := range m {
		if _, found := m[n-1]; found {
			continue
		}
		length := 1
		curr := n + 1
		for {
			if _, found := m[curr]; found {
				length++
				curr++
			} else {
				break
			}
		}

		if length > lcs {
			lcs = length
		}
	}
	return lcs
}
