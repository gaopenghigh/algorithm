/**
437. 路径总和 III
难度 中等
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
示例 2：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
*/

/**
假设 f(node, target) 表示以 node 为起点的路径总和为 target 的路径的数目，则
if node.val == target:
	f(node, target) = f(node.left, target - node.val) + f(node.right, target - node.val) + 1
else:
	f(node, target) = f(node.left, target - node.val) + f(node.right, target - node.val)
Base Case:
f(nil, target) = 0

最终的结果则为：
sum(
	以 root 为起点的路径总和为 target 的路径数目，即 f(root, target),
	不以 root 为起点的路径总和为 target 的路径数目，又可以进一步分为：
	root.Left 树中的路径总和为 target 的路径数目，
	root.Right 树中的路径总和为 target 的路径数目，
)
*/

package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, targetSum int) int {
	if root == nil {
		return 0
	}
	res := f(root, targetSum)
	res = res + pathSum(root.Left, targetSum)
	res = res + pathSum(root.Right, targetSum)
	return res
}

func f(root *TreeNode, target int) int {
	if root == nil {
		return 0
	}
	var r int
	if root.Val == target {
		r = 1 + f(root.Left, target-root.Val) + f(root.Right, target-root.Val)
	} else {
		r = f(root.Left, target-root.Val) + f(root.Right, target-root.Val)
	}
	return r
}
