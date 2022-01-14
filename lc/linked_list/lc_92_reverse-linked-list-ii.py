# 92. 反转链表 II
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。


# 算法本身并不难，难的是细节处理。一个避免出错的方法是老老实实找到需要反转的链表的头和尾，同时老老实实记录下该子链表的前驱结点和后驱节点。然后将子链表当做一个独立的字符串反转，最后再和前驱以及后驱节点连在一起。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f'Node({self.val})'

def printListNode(head):
    while head is not None:
        print(head, '--> ', end='')
        head = head.next
    print('None')

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head

        pre = dummy
        pos = 1
        p = head
        while pos < left:
            pos += 1
            pre = p
            p = p.next
        
        start = p
        while pos < right:
            pos += 1
            p = p.next
        end = p
        successor = end.next
        # print(f'pre={pre}, start={start}, end={end}, successor={successor}')

        subpre = None
        curr = start
        while curr != successor:
            next = curr.next
            curr.next = subpre
            subpre = curr
            curr = next
        
        start.next = successor
        pre.next = end
        return dummy.next


if __name__ == '__main__':
    head = ListNode(0)
    n = head
    for i in range(1, 8):
        n.next = ListNode(i)
        n = n.next
    printListNode(head)

    head = Solution().reverseBetween(head, 1, 1)
    printListNode(head)