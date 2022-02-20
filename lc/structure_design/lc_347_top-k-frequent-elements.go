/**
347. 前 K 个高频元素
难度 中等
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

提示：
1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
*/

/**
前 K 个高频元素，考虑使用大小为 K 的小根堆。
*/

package main

func topKFrequent(nums []int, k int) []int {
	m := make(map[int]int)
	for _, num := range nums {
		if _, found := m[num]; !found {
			m[num] = 1
		} else {
			m[num] = m[num] + 1
		}
	}
	h := NewMinHeap(k)
	for num, cnt := range m {
		h.Add(Element{val: num, count: cnt})
	}
	res := make([]int, 0, k)
	for _, e := range h.All() {
		res = append(res, e.val)
	}
	return res
}

type Element struct {
	count int
	val   int
}

type MinHeap struct {
	datas []Element
	size  int
}

func NewMinHeap(k int) *MinHeap {
	return &MinHeap{
		datas: make([]Element, 0, k),
		size:  k,
	}
}

func (h *MinHeap) swim(idx int) {
	var parent int
	for (idx-1)/2 >= 0 {
		parent = (idx - 1) / 2
		if h.datas[parent].count > h.datas[idx].count {
			h.datas[parent], h.datas[idx] = h.datas[idx], h.datas[parent]
			idx = parent
		} else {
			break
		}
	}
}

func (h *MinHeap) sink(idx int) {
	for idx*2+1 < len(h.datas) {
		smallest := idx
		left := idx*2 + 1
		right := idx*2 + 2
		if left < len(h.datas) && h.datas[left].count < h.datas[smallest].count {
			smallest = left
		}
		if right < len(h.datas) && h.datas[right].count < h.datas[smallest].count {
			smallest = right
		}
		if smallest != idx {
			h.datas[idx], h.datas[smallest] = h.datas[smallest], h.datas[idx]
			idx = smallest
		} else {
			break
		}
	}
}

func (h *MinHeap) Add(e Element) {
	if len(h.datas) >= h.size {
		if e.count < h.datas[0].count {
			return
		}
		h.Pop()
	}
	h.datas = append(h.datas, e)
	h.swim(len(h.datas) - 1)
}

func (h *MinHeap) Pop() Element {
	top := h.datas[0]
	h.datas[0] = h.datas[len(h.datas)-1]
	h.datas = h.datas[0 : len(h.datas)-1]
	h.sink(0)
	return top
}

func (h *MinHeap) All() []Element {
	return h.datas
}
