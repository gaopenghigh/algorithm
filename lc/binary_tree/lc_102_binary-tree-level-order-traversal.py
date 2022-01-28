# 102. 二叉树的层序遍历
# 难度 中等
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
# 
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]

# 就是 BFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []
        res = []
        q = []
        q.append(root)
        while q:
            size = len(q)
            row = []
            for _ in range(size):
                node = q.pop(0)
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(row)
        return res
