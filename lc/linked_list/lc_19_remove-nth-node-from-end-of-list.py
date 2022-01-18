# 19. 删除链表的倒数第 N 个结点
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点

# 使用双指针，fast 比 slow 快 n 步

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
        