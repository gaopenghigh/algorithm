# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
# 
# 提醒一下，二叉搜索树满足下列约束条件：
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
# 
# 链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree


# 对于一个节点，大于等于它的节点，一定在它的右子树。所以可以使用中序遍历，并且先访问右节点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root

    def traverse(self, root):
        if root is None:
            return None
        self.traverse(root.right)
        self.sum += root.val
        root.val = self.sum
        self.traverse(root.left)
        