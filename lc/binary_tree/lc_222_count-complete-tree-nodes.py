# 222. 完全二叉树的节点个数
# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
# 完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

# 对于普通二叉树，递归计算，当前 root 的节点个数 = 1 + 左子树节点个数 + 右子树节点个数
# 对于满二叉树，假设树的高度是 h ，则节点个数为 2*h - 1
# 所有优化点就是针对满二叉树做一下特殊判断，由于题中给的树是完全二叉树，只要它的左右子树高度相同，则一定是满二叉树。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        leftHight = 0
        node = root.left
        while node is not None:
            node = node.left
            leftHight += 1

        rightHight = 0
        node = root.right
        while node is not None:
            node = node.right
            rightHight += 1

        if leftHight == rightHight:
            return 2**(leftHight + 1) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)