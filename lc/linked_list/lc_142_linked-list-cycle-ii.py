# 142. 环形链表 II
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 不允许修改 链表。
# 
# 示例 1：
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 示例 2：
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 示例 3：
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#  
# 提示：
# 链表中节点的数目范围在范围 [0, 104] 内
# -105 <= Node.val <= 105
# pos 的值为 -1 或者链表中的一个有效索引

# 最直观的方式是用一个 map 存储一个节点是否被访问过。
# 比较技巧的方式是使用双指针，需要先做一点数学推导，并不直观。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        while head is not None:
            if head in s:
                return head
            s.add(head)
            head = head.next
        return None