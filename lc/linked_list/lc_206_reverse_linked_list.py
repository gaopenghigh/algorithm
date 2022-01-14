# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        print(self.val)
        if self.next is not None:
            self.next.print()

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre

if __name__ == '__main__':
    head = ListNode(0)
    n = head
    for i in range(1, 8):
        n.next = ListNode(i)
        n = n.next
    head.print()

    print("--")
    head = Solution().reverseList(head)
    head.print()