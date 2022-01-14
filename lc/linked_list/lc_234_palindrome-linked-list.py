# https://leetcode-cn.com/problems/palindrome-linked-list/
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

# 先用快慢指针找到链表中点，将后半部分链表反转，然后和前半部分比较是否一致。由于链表长度可能为奇数或偶数，细节上需要小心处理一下。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next is None:
            return True

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # 链表长度为奇数
        if fast is not None:
            slow = slow.next

        reversedList = self.reverseList(slow)
        p1 = reversedList
        p2 = head
        while p1 is not None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    
    def reverseList(self, head):
        pre = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre