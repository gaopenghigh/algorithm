# 144. 二叉树的前序遍历
# 难度 简单
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverse(res, root)
        return res
    def traverse(self, res, root):
        if not root:
            return
        res.append(root.val)
        self.traverse(res, root.left)
        self.traverse(res, root.right)

