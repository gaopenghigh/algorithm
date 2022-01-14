# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
# 
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 初始状态下，所有 next 指针都被设置为 NULL。
# 
# 进阶：
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

# 这个题的关键点是将两个节点传入递归函数中

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return None
        self.connectTwoNode(root.left, root.right)
        return root

    def connectTwoNode(self, p, q):
        if p is None or q is None:
            return
        p.next = q
        self.connectTwoNode(p.left, p.right)
        self.connectTwoNode(q.left, q.right)
        self.connectTwoNode(p.right, q.left)


# 另外一种比较容易想到的解法是使用 BFS，把位于同一层的 node 给连起来

class Solution2:
    def connect(self, root: Node) -> Node:
        if root is None:
            return None
        q = []
        q.append(root)
        while len(q) > 0:
            i = 0
            sizeInThisLevel = len(q)
            pre = None
            while i < sizeInThisLevel:
                i += 1
                node = q.pop(0)
                if pre is not None:
                    pre.next = node
                pre = node
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return root

