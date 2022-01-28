# 94. 二叉树的中序遍历
# 难度 简单
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
# 
# 示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 
# 示例 2：
# 输入：root = []
# 输出：[]
# 
# 示例 3：
# 输入：root = [1]
# 输出：[1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        self.traverse(res, root)
        return res
    def traverse(self, res, node: TreeNode):
        if node is None:
            return
        self.traverse(res, node.left)
        res.append(node.val)
        self.traverse(res, node.right)