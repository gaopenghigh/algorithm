/**
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
*/

package main

import (
	"container/list"
	"fmt"
)

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// BFS
func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	depth := 0
	q := list.New()
	q.PushBack((root))
	for q.Len() > 0 {
		size := q.Len()
		depth += 1
		for i := 0; i < size; i++ {
			e := q.Front()
			q.Remove(e)
			node := e.Value.(*TreeNode)
			if node.Left == nil && node.Right == nil {
				return depth
			}
			if node.Left != nil {
				q.PushBack((node.Left))
			}
			if node.Right != nil {
				q.PushBack((node.Right))
			}
		}
	}
	return depth
}

func main() {
	root := TreeNode{}
	root.Left = &TreeNode{Val: 1}
	root.Right = &TreeNode{Val: 1}
	fmt.Println(minDepth(&root))
}
