# 124. 二叉树中的最大路径和
# 难度 困难
# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
# 
# 示例 1：
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
# 
# 示例 2：
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


# 使用类似于动态规划的思路
# 这题目的难点在于理解题意和转化题意。
# 我们可以结合 数组的最大子数组和 的思路去解题。
# 
# 1. 「可以从任意节点出发, 到达任意节点」 的路径, 
#    一定是先上升（ 0 ～ n 个）节点, 到达顶点, 后下降（ 0 ～ n 个）节点。
#    我们可以通过枚举顶点的方式来枚举路径。
#    
# 2. 我们枚举顶点时, 可以把路径分拆成3部分： 左侧路径、右侧路径和顶点。
#    如下面的路径, 顶点为 20, 左侧路径为 6 -> 15, 右侧为 6 -> 7。
#    
#       -10
#       / \
#      9 [20]
#        /  \
#      [15] [7]
#      /    / \
#    [6]   4  [6]   
# 
#    以当前节点为顶点的路径中, 最大和为 两侧路径的最大和 + 节点的值。
#    需要注意的是, 两侧路径也可能不选, 此时取 0。
# 
# 3. 如何求两侧路径最大和？ 看一个类似问题：求数组的最大子数组和。
#    动态规划： dp[i] 代表以 nums[i] 为结尾的子数组的最大和。
#    转移方程： dp[i] = max(dp[i-1], 0) + nums[i]。
# 
# 4. 在树上, 设 dp[C] 代表以当前节点为结尾的最大上升路径和, 
#    则我们需要对节点的左右子树做一个选择, 有
#    dp[C] = max(max(dp[L], 0), max(dp[R], 0)) + C.val
#    式中, C,L,R 分别代指 当前节点、左子节点、右子节点。
# 
# 5. 最后, 以当前节点为顶点的路径中, 最大的和为
#    max(dp[L], 0) + max(dp[R], 0) + C.val。
#    我们枚举顶点, 并记录最大答案。


import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.cache = {}
        self.maxSum = -sys.maxsize

    def maxPathSum(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.maxSum

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.traverse(root.right)
        maxSum = max(self.dp(root.left), 0) + max(self.dp(root.right), 0) + root.val
        if maxSum > self.maxSum:
            self.maxSum = maxSum

    def dp(self, root):
        if root is None:
            return -sys.maxsize
        if root in self.cache:
            return self.cache[root]
        res = max(
            max(self.dp(root.left), 0),
            max(self.dp(root.right), 0)
        ) + root.val
        self.cache[root] = res
        return res

