# 230. 二叉搜索树中第K小的元素
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

# 中序遍历，遍历时同时在全局变量中记录遍历到第几个了

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.rank = 0
        self.res = None

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.traverse(root, k)
        return self.res

    def traverse(self, root, k):
        if root is None:
            return None
        self.traverse(root.left, k)
        self.rank += 1
        if self.rank == k:
            self.res = root.val
            return
        self.traverse(root.right, k)