/**
148. 排序链表
难度 中等
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
*/

/**
最直接的方法是插入排序，但不满足题目要求的时间复杂度。
考虑用归并排序
*/

package main

import "fmt"

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// 使用归并排序
func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	// 减为左右两段，分别排序，然后合并
	slow, fast := head, head.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	left := head
	right := slow.Next
	slow.Next = nil
	l := sortList(left)
	r := sortList(right)

	dummyHead := &ListNode{}
	pre := dummyHead
	for l != nil && r != nil {
		if l.Val < r.Val {
			pre.Next = l
			l = l.Next
		} else {
			pre.Next = r
			r = r.Next
		}
		pre = pre.Next
	}
	if l != nil {
		pre.Next = l
	}
	if r != nil {
		pre.Next = r
	}

	return dummyHead.Next
}

// 使用插入排序
func sortList2(head *ListNode) *ListNode {
	var r *ListNode
	for head != nil {
		node := head
		head = head.Next
		r = insert(r, node)
	}
	return r
}

func insert(head, node *ListNode) *ListNode {
	dummyHead := &ListNode{}
	dummyHead.Next = head
	curr := dummyHead.Next
	pre := dummyHead
	for {
		if curr == nil || curr.Val > node.Val {
			pre.Next = node
			node.Next = curr
			break
		}
		pre = curr
		curr = curr.Next
	}
	return dummyHead.Next
}

func main() {
	head := &ListNode{1, nil}
	head.Next = &ListNode{2, nil}
	head.Next.Next = &ListNode{3, nil}
	r := sortList(head)
	for r != nil {
		fmt.Println(r.Val)
		r = r.Next
	}
}
