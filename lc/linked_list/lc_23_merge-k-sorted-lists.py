# 23. 合并K个升序链表
# https://leetcode-cn.com/problems/merge-k-sorted-lists/
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# 优化点是使用一个小根堆（优先级队列）来加速从 k 个链表的头结点中选择最小的一个。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MinHeap:
    def __init__(self) -> None:
        self.data = []
        self.length = 0
    
    def _sink(self, i):
        while i * 2 + 1 < self.length:
            l = i * 2 + 1
            r = i * 2 + 2
            smallest = i
            if l < self.length and self.data[l].val < self.data[smallest].val:
                smallest = l
            if r < self.length and self.data[r].val < self.data[smallest].val:
                smallest = r
            if smallest != i:
                self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
                i = smallest
            else:
                return

    def _swim(self, i):
        ancestor = (i - 1) // 2
        while ancestor >= 0:
            if self.data[ancestor].val > self.data[i].val:
                self.data[ancestor], self.data[i] = self.data[i], self.data[ancestor]
                i = ancestor
                ancestor = (i - 1) // 2
            else:
                return

    def add(self, node: ListNode):
        self.data.append(node)
        self.length += 1
        self._swim(self.length - 1)

    def pop(self) -> ListNode:
        if self.length == 0:
            return None
        smallest = self.data[0]
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        last = self.data.pop()
        self.length -= 1
        self._sink(0)
        return smallest

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        pq = MinHeap()
        for l in lists:
            if l is not None:
                pq.add(l)

        dummyHead = ListNode()
        p = dummyHead
        
        while pq.length > 0:
            smallest = pq.pop()
            p.next = smallest
            if smallest.next is not None:
                pq.add(smallest.next)
            p = p.next
        return dummyHead.next


if __name__ == '__main__':
    int_lists = [[1,4,5],[1,3,4],[2,6]]
    node_lists = []
    for int_list in int_lists:
        dummy = ListNode()
        p = dummy
        for i in int_list:
            p.next = ListNode(i)
            p = p.next
        node_lists.append(dummy.next)

    r = Solution().mergeKLists(node_lists)
    print(r)
    while r is not None:
        print(r.val)
        r = r.next