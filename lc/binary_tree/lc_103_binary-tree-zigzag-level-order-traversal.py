# 103. 二叉树的锯齿形层序遍历
# 难度 中等
# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]

# BFS，每隔一行 reverse 一下

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []
        res = []
        q = []
        q.append(root)
        shouldReverse = False
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
            if shouldReverse:
                row.reverse()
            shouldReverse = not shouldReverse
            res.append(row)
        return res
