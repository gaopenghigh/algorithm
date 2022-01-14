# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# https://leetcode-cn.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        n1 = list1
        n2 = list2
        dummyHead = ListNode()
        p = dummyHead
        while n1 is not None and n2 is not None:
            if n1.val <= n2.val:
                p.next = n1
                n1 = n1.next
            else:
                p.next = n2
                n2 = n2.next
            p = p.next
        while n1 is not None:
            p.next = n1
            n1 = n1.next
            p = p.next
        while n2 is not None:
            p.next = n2
            n2 = n2.next
            p = p.next
        return dummyHead.next