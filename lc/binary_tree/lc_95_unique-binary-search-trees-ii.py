# 95. 不同的二叉搜索树 II
# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

# 随意选一个数作为 root，则它的左子树由所有小于它的节点组成，它的右子树由所有大于它的节点组成。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        return self.build(1, n)
    
    # 构建所有使用从 low 到 high 的节点组成的 BST
    def build(self, low, high):
        res = []
        if low > high:
            res.append(None)
            return res
         
        for i in range(low, high + 1):
            leftTrees = self.build(low, i - 1)
            rightTrees = self.build(i + 1, high)
            # 为 root 组合所有的 left 和 right
            for left in leftTrees:
                for right in rightTrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res
