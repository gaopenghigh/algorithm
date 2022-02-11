# 199. 二叉树的右视图
# 难度 中等
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 示例 1:
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
# 
# 示例 2:
# 输入: [1,null,3]
# 输出: [1,3]
# 
# 示例 3:
# 输入: []
# 输出: []


# BFS 取每层的最右边一个

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        return self.bfs(root)

    def bfs(self, root):
        if not root:
            return []
        res = []
        q = []
        q.append(root)
        while q:
            size = len(q)
            node = None
            for _ in range(size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)
        return res

        

