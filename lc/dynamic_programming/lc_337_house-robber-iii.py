# 337. 打家劫舍 III
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

# 类似 198，状态转移方程需要修改一下
# dp(root) = x 表示对 根为 root 的二叉树进行行动所得的最大金额
# 对于 root，要么偷要么不偷
# 如果偷，则所得为 root.val + dp(root.left.left) + dp(root.left.right) + dp(root.right.left) + dp(root.right.right) 
# 如果不偷，则所得为 dp(root.left) + dp(root.right)
# base case 就是 dp(None) = 0

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.cache = {}
    
    def dp(self, root):
        if root is None:
            return 0
        if root in self.cache:
            return self.cache[root]
        # 偷
        do = root.val
        if root.left:
            do = do + self.dp(root.left.left) + self.dp(root.left.right)
        if root.right:
            do = do + self.dp(root.right.left) + self.dp(root.right.right)
        # 不偷
        not_do = self.dp(root.left) + self.dp(root.right)
        r = max(do, not_do)
        self.cache[root] = r
        return r

    def rob(self, root: TreeNode) -> int:
        return self.dp(root)