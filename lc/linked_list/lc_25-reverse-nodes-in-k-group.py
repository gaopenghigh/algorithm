# 25. K 个一组翻转链表
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 进阶：
# 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#  
# 
# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 
# 示例 2：
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
# 
# 示例 3：
# 输入：head = [1,2,3,4,5], k = 1
# 输出：[1,2,3,4,5]
# 
# 示例 4：
# 输入：head = [1], k = 1
# 输出：[1]
# 提示：
# 
# 列表中节点的数量在范围 sz 内
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz
# 
# 链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group/


# 每 k 个节点为一组，记录这一组之前的节点 pre 和这一组之后的节点 next
# 然后将这一组链表翻转，得到 head 和 tail，然后设置 pre.next = head, tail.next = next, pre = tail
# 一个技巧就是添加一个“假”的 head
# 子链表的翻转，可以原地翻转，或者使用一个栈进行翻转

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f'Node({self.val})'

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        fackHead = ListNode(-1)
        fackHead.next = head
        pre = fackHead
        tail = pre

        while head is not None:
            tail = pre
            print(f'head={head}, tail={tail}')
            for i in range(k):
                tail = tail.next
                if tail is None:
                    return fackHead.next
            next = tail.next
            group_head, group_tail = self.reverseSubList(head, tail)
            group_tail.next = next
            pre.next = group_head
            pre = group_tail
            head = next
        return fackHead.next

    # 翻转一个子链表，并且返回新的头与尾
    def reverseSubList(self, head, tail):
        print(f'reverse sub head {head}, tail {tail}')
        pre = None
        curr = head
        while pre != tail:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre, head


# 使用一个栈来实现反转子链表
class Solution2:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        stack = []
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        curr = head
        while curr is not None:
            next = curr.next
            stack.append(curr)
            if len(stack) == k:
                group_head, group_tail = self._list_in_stack(stack)
                pre.next = group_head
                pre = group_tail
            curr = next
        if len(stack) > 0:
            pre.next = stack[0]
        return dummy.next
    
    # 从 stack 中逐个弹出元素组成链表，返回头和尾
    def _list_in_stack(self, stack):
        head = stack.pop()
        pre = head
        while len(stack) > 0:
            node = stack.pop()
            pre.next = node
            pre = node
        pre.next = None
        return head, pre

def _print_node(head):
    vals = []
    n = head
    while n is not None:
        print(f' --> {n.val}')
        n = n.next

if __name__ == '__main__':
    head = ListNode(1)
    n = head
    for i in range(2, 7):
        n.next = ListNode(i)
        n = n.next
    _print_node(head)
    print('----')

    head = Solution2().reverseKGroup(head, 3)
    print('----')
    _print_node(head)