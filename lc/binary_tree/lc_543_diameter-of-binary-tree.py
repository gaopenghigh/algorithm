# 543. 二叉树的直径
# 难度 简单
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
# 示例 :
# 给定二叉树
# 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。


# 遍历所有节点，计算经过每个节点的深度，同时计算最长路径的长度（经过的节点数 - 1），使用一个全局变量记录最大值。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.ans = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.ans - 1

    # 返回以 root 为 根的树的高度，计算的过程中同时计算直径
    def traverse(self, root):
        if not root:
            return 0
        leftHeight = self.traverse(root.left) 
        rightHeight = self.traverse(root.right)
        diameter = leftHeight + rightHeight + 1
        if diameter > self.ans:
            self.ans = diameter
        return max(leftHeight, rightHeight) + 1
