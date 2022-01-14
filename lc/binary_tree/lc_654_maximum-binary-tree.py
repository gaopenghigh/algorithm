# 654. 最大二叉树
# 给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：
# 二叉树的根是数组 nums 中的最大元素。
# 左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
# 右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
# 返回有给定数组 nums 构建的 最大二叉树 。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        max_index = self.find_max_index(nums)
        max_n = nums[max_index]
        root = TreeNode(max_n)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return root

    def find_max_index(self, nums):
        m = -1
        max_index = 0
        for i, n in enumerate(nums):
            if n > m:
                m = n
                max_index = i
        return max_index
