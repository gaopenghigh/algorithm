# 98. 验证二叉搜索树
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 
# 有效 二叉搜索树定义如下：
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 注意，根据 BST 的定义，root的整个左子树都要小于root.val，整个右子树都要大于root.val。
# 所以不能简单地判断左子节点值小于当前节点，右子节点值大于当前节点。
# 这个题的难度在于想办法把这些限制信息通过递归的方式传递下去。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.traverse(root, None, None)

    def traverse(self, root, minVal, maxVal):
        if root is None:
            return True
        if minVal is not None and root.val <= minVal:
            return False
        if maxVal is not None and root.val >= maxVal:
            return False
        if not self.traverse(root.left, minVal, root.val):
            return False
        if not self.traverse(root.right, root.val, maxVal):
            return False
        return True