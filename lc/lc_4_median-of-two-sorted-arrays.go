/**
4. 寻找两个正序数组的中位数
难度: 困难
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000
*/

/**
假设 merged 为合并后升序的数组，则
m+n 为奇数时，中位数是，merged[(m+n-1)/2]
m+n 为偶数是，中位数的索引是合并排序后数组的 (merged[(m+n)/2-1] + merged[m+n]) / 2
所以只需要从两个数组中一直取最小的，知道去到我们需要的那个位置或者那2个位置即可。但这种方法时间复杂度还是 O(m+n)。

如果对时间复杂度的要求有 log ⁡，通常都需要用到二分查找，这道题也可以通过二分查找实现。
题目变成类似 215 题，从数组中找到第 k 小的数字。
假设 nums1 的前 k/2 比 nums2 的第 k/2 个数字，也就是 nums2[k/2]小，那么 nums1 的前 k/2 个元素肯定不是第 k 小的元素，因为 nums2[:k/2] 中的每个元素也都比 nums2[k/2] 小。
*/

package main

import "fmt"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	m := len(nums1)
	n := len(nums2)
	midLeft, midRight := 0, 0
	// m + n 为偶数
	if (m+n)%2 == 0 {
		midLeft = (m+n)/2 - 1
		midRight = (m + n) / 2
	} else {
		midLeft = (m + n - 1) / 2
		midRight = midLeft
	}
	left := 0
	right := 0
	mergedIndex := 0
	i, j := 0, 0
	for i < m && j < n {
		n1 := nums1[i]
		n2 := nums2[j]
		min := n1
		if n1 < n2 {
			i++
		} else {
			j++
			min = n2
		}

		if mergedIndex == midLeft {
			left = min
		}
		if mergedIndex == midRight {
			right = min
			return (float64(left) + float64(right)) / float64(2)
		}
		mergedIndex++
	}

	for i < m {
		if mergedIndex == midLeft {
			left = nums1[i]
		}
		if mergedIndex == midRight {
			right = nums1[i]
			return (float64(left) + float64(right)) / float64(2)
		}
	}
	for j < n {
		if mergedIndex == midLeft {
			left = nums2[j]
		}
		if mergedIndex == midRight {
			right = nums2[j]
			return (float64(left) + float64(right)) / float64(2)
		}
	}

	return (float64(left) + float64(right)) / float64(2)
}

func main() {
	nums1 := []int{1, 1}
	nums2 := []int{2}
	fmt.Println(findMedianSortedArrays(nums1, nums2))
}
