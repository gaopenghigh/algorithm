# 2. 两数相加
# 难度 中等
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例 1：
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# 
# 示例 2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 
# 示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        pre = dummy
        up = 0
        while l1 and l2:
            r = l1.val + l2.val + up
            up = 0
            if r > 9:
                r = r - 10
                up = 1
            pre.next = ListNode(r)
            pre = pre.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            r = l1.val + up
            up = 0
            if r > 9:
                r = r - 10
                up = 1
            pre.next = ListNode(r)
            pre = pre.next
            l1 = l1.next
        while l2:
            r = l2.val + up
            up = 0
            if r > 9:
                r = r - 10
                up = 1
            pre.next = ListNode(r)
            pre = pre.next
            l2 = l2.next
        if up > 0:
            pre.next = ListNode(up)
        return dummy.next
