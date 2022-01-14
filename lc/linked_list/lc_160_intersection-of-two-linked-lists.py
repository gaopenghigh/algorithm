# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
# 160. 相交链表
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

# 分别遍历两个列表，得到它们的长度差 k。再重头遍历两个链表，但较长的一个链表先走 k 步。此时两个指针指向的位置里链表尾部距离一样，找到第一个相等的元素即可。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        lenA = 0
        lenB = 0
        while pA is not None:
            lenA += 1
            pA = pA.next
        while pB is not None:
            lenB += 1
            pB = pB.next

        pA = headA
        pB = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                pA = pA.next
        else:
            for i in range(lenB - lenA):
                pB = pB.next
        
        while pA is not None and pB is not None:
            if pA == pB:
                return pA
            else:
                pA = pA.next
                pB = pB.next

        return None
