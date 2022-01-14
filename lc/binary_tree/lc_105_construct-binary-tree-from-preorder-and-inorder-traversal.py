# 105. 从前序与中序遍历序列构造二叉树
# 给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。

# 关键点在于理解前序遍历和中序遍历结果的特点。参考 https://labuladong.gitee.io/algo/2/18/23/
# 下面的代码在递归时使用了值传递，这样函数更加简洁，可以改为传递引用加 index 位置以提升效率

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)

        if len(preorder) == 1:
            return root

        root_pos_in_inorder = 0
        for i, v in enumerate(inorder):
            if v == root_val:
                root_pos_in_inorder = i
                break
        
        left_len = root_pos_in_inorder

        left_preorder = preorder[1:left_len + 1]
        right_preorder = preorder[left_len+1:]
        left_inorder = inorder[:root_pos_in_inorder]
        right_inorder = inorder[root_pos_in_inorder+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root