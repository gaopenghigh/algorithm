# 106. 从中序与后序遍历序列构造二叉树
# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 注意:
# 你可以假设树中没有重复的元素。

# 思路和 105 一样

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        if len(inorder) == 1:
            return root

        root_pos_in_inorder = 0
        for i, v in enumerate(inorder):
            if v == root_val:
                root_pos_in_inorder = i
                break

        left_len = root_pos_in_inorder
        left_inorder = inorder[:root_pos_in_inorder]
        right_inorder = inorder[root_pos_in_inorder+1:]
        left_postorder = postorder[:left_len]
        right_postorder = postorder[left_len:-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root