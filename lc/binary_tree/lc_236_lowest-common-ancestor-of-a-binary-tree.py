# 236. 二叉树的最近公共祖先
# 中等
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 示例 1：
#输入：root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
#输出：3
#解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
#
#示例 2：
#输入：root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4
#输出：5
#解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
#
#示例 3：
#输入：root = [1,2], p = 1, q = 2
#输出：1
#
# 提示：
# 树中节点数目在范围 [2, 105] 内。
# -109 <= Node.val <= 109
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。
# 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree

# 网上大多数的解法以及 LeetCode 官方的解法都不够直观，不容易理解。
# 下面的解法更容易理解，时间复杂度也一样，代码稍微复杂一点点，但容易理解多了。
# 如果 node 是 p 和 q 的最小公共祖先，有几种情况：
# 1. node 就是 p，然后以 node.left 或 node.right 为根的树中包含了 q
# 2. node 就是 q，然后以 node.left 或 node.right 为根的树中包含了 p
# 3. node != p 并且 node != q，以 node.left 为根的树中包含了 p，以 node.right 为根的树中包含了 q
# 4. node != p 并且 node != q，以 node.left 为根的树中包含了 q，以 node.right 为根的树中包含了 p
# 所以可以看到，问题可以分解为对 root 本身的比较，以及对它左右子树的判断：
# 如果在左右子树中分别找到了 p 和 q，那 root 肯定是最小公共祖先
# 如果 root 自己就是 p 和 q 之一，并且在左右子树中找到了另外一个，则 root 也是最小公共祖先

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        return 'Node(%d)' % self.val

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor, foundP, foundQ = self.dfs(root, p, q)
        return ancestor

    # dfs return 3 values, lowestCommonAncestor, foundP(bool) and foundQ(bool)
    def dfs(self, root, p, q): 
        if root is None:
            return None, False, False
        ancestor, foundPLeft, foundQLeft = self.dfs(root.left, p, q)
        if ancestor is not None:
            return ancestor, True, True
        ancestor, foundPRight, foundQRight = self.dfs(root.right, p, q)
        if ancestor is not None:
            return ancestor, True, True
        foundP, foundQ = False, False
        if root.val == p.val or (foundPLeft or foundPRight):
            foundP = True
        if root.val == q.val or (foundQLeft or foundQRight):
            foundQ = True
        if foundP and foundQ:
            return root, True, True
        return None, foundP, foundQ
