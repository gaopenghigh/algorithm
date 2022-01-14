# 450. 删除二叉搜索树中的节点
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
# 一般来说，删除节点可分为两个步骤：
# 首先找到需要删除的节点；
# 如果找到了，删除它。

# 关键点在于删除一个节点后，找到它的右子树中最小的一个节点来代替它。
# 会有一些细节需要处理，一个不容易出错的原理就是拆分成独立的小函数

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return
        
        if key == root.val:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            left = root.left
            right = root.right

            smallest, newRight = self.pop_smallest(root.right)
            smallest.left = left
            smallest.right = newRight
            return smallest
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        
    def pop_smallest(self, root):
        if root is None:
            return None
        if root.left is None:
            newRoot = root.right
            smallest = root
            smallest.left = None
            smallest.right = None
            return smallest, newRoot

        node = root
        pre = None
        while node.left is not None:
            pre = node
            node = node.left
        pre.left = node.right

        node.right = None
        return node, root
        