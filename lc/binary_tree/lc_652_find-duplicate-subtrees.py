# 652. 寻找重复的子树
# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
# 两棵树重复是指它们具有相同的结构以及相同的结点值。

# 要判断是否有重复的树，就需要知道一棵树长什么样，也就是对一个数做序列化。
# 最简单的方法就是使用前序、中序、后序遍历中的一种遍历这棵树，然后把遍历的结果存为一个字符串。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.res = []
        self.memo = {}
        
    def findDuplicateSubtrees(self, root: TreeNode) -> TreeNode:
        self._find_and_record(root)
        return self.res

    def _find_and_record(self, root):
        if root is None:
            return '#'
        left = self._find_and_record(root.left)
        right = self._find_and_record(root.right)
        serialize_str = f'{left},{right},{root.val}'
        if serialize_str not in self.memo:
            self.memo[serialize_str] = 1
        elif self.memo[serialize_str] == 1:
            self.res.append(root)
            self.memo[serialize_str] += 1
        else:
            self.memo[serialize_str] += 1
        return serialize_str