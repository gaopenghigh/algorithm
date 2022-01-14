# 876. 链表的中间结点
# https://leetcode-cn.com/problems/middle-of-the-linked-list/
# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。

# 使用快慢指针，快的一次走 2 步，慢的一次走 1 步

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    