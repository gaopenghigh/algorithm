# 143. 重排链表
# 难度 中等
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 示例 1：
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
# 
# 示例 2：
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]


# 有 2 个方法，方法 1 是转换成数组，然后使用双指针重组链表。
# 方法 2 是先找到链表中点，拆分为左右两段，然后把右边链表翻转，最后把两条链表合并

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        node = head
        while node:
            arr.append(node)
            node = node.next
        left = 0
        right = len(arr) - 1 
        while left < right:
            arr[left].next = arr[right]
            left += 1
            if left == right:
                break
            arr[right].next = arr[left]
            right -= 1
        arr[left].next = None


class Solution2:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        mid = self.findMid(head)
        left = head
        right = self.reverseList(mid.next)
        mid.next = None
        self.merge(left, right)
    
    def findMid(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        pre = None
        curr = head
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre
    
    def merge(self, l1, l2):
        while l1 and l2:
            l1Next = l1.next
            l2Next = l2.next
            l1.next = l2
            l1 = l1Next
            l2.next = l1
            l2 = l2Next
        

