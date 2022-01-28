# 110. 平衡二叉树
# 难度 简单
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

# 使用递归的方法，小心仔细即可

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        balance, _ = self._balance(root)
        return balance

    def _balance(self, node) -> tuple[bool, int]:
        if node is None:
            return True, 0
        leftBalance, leftHight = self._balance(node.left)
        rightBalance, rightHight = self._balance(node.right)
        hight = max(leftHight, rightHight) + 1
        return leftBalance and rightBalance and abs(leftHight - rightHight) <= 1, hight