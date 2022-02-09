/*
698. 划分为k个相等的子集
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
示例 1：
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
*/

package main

import (
	"fmt"
)

/*
回溯算法做选择时，尽可能地让每次可选的少一点，宁可选择的次数多一点。而不是每次从很多个选择中选一个。
也就是尽量让选择树瘦长，而不是扁宽。
k 个子集想象为 k 个桶，我们一个桶一个桶地装，把一个桶刚好装到 target 就下一个桶。
*/

var (
	g_nums  []int
	used    map[int]bool
	target  int
	buckets []int
)

func canPartitionKSubsets(nums []int, k int) bool {
	sum := 0
	for _, n := range nums {
		sum += n
	}
	if sum%k != 0 {
		return false
	}
	if len(nums) < k {
		return false
	}
	g_nums = nums
	target = sum / k
	buckets = make([]int, k)
	used = make(map[int]bool, len(nums))
	for i := 0; i < len(nums); i++ {
		used[i] = false
	}
	return backtrack(0, 0)
}

/*
buckets 为所有的桶，bucketIndex 为桶号，startFrom 表示只考虑 nums[startFrom:] 内的数字，之前的数字，要么已经加入这个桶了，要么别用其他桶用掉了，要么太大了，由于桶肯定越来越满，所以如果这个数字之前就太大了，则之后肯定不可能加到这个桶里面去。
*/
func backtrack(bucketIndex int, startFrom int) bool {
	// fmt.Println("bucketIndex=", bucketIndex, "startFrom=", startFrom, "buckets=", buckets, "used=", used)
	// 已经选择到了最后一个桶,由于之前的桶也被装满了，而 target = sum/k，所以所有的 num 也被用完了
	if bucketIndex == len(buckets)-1 {
		return true
	}

	// 当前桶装满了，装下一个桶
	curr := buckets[bucketIndex]
	if curr == target {
		return backtrack(bucketIndex+1, 0)
	}

	for i := startFrom; i < len(g_nums); i++ {
		if used[i] {
			continue
		}
		n := g_nums[i]
		if curr+n > target {
			continue
		}

		buckets[bucketIndex] += n
		used[i] = true
		// 考虑下一个数是否装入当前桶
		if backtrack(bucketIndex, i+1) {
			return true
		}
		buckets[bucketIndex] -= n
		used[i] = false
	}
	return false
}

func main() {
	/**
		nums := []int{815, 625, 3889, 4471, 60, 494, 944, 1118, 4623, 497, 771, 679, 1240, 202, 601, 883}
		k := 3
	nums := []int{10, 5, 5, 4, 3, 6, 6, 7, 6, 8, 6, 3, 4, 5, 3, 7}
	k := 8
	nums := []int{4, 3, 2, 3, 5, 2, 1}
	k := 4
	*/
	nums := []int{1, 2, 3, 4}
	k := 2
	fmt.Println(canPartitionKSubsets(nums, k))
}
