# 146. LRU 缓存
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
# 
# 示例：
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  
# 
# 提示：
# 1 <= capacity <= 3000
# 0 <= key <= 10000
# 0 <= value <= 105
# 最多调用 2 * 105 次 get 和 put

# 使用双向链表来存储具体数据，加上一个 dict 来存储到双向链表节点的引用
class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
    
    def __str__(self) -> str:
        next_key = f'{self.next.key}' if self.next is not None else None
        pre_key = f'{self.pre.key}' if self.pre is not None else None
        return f'Node(key={self.key}, value={self.val}, next_key={next_key}, pre_key={pre_key})'

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.size = 0
        # dummy head and tail
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def _move_to_head(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = self.head.next
        self.head.next.pre = node
        node.pre = self.head
        self.head.next = node
    
    def _del_tail(self):
        node = self.tail.pre
        node.pre.next = self.tail
        self.tail.pre = node.pre
        self.keys.pop(node.key)
        del(node)
        self.size -= 1
    
    def _print_data(self):
        node = self.head
        print('---')
        while node is not None:
            print(node)
            node = node.next
        print('---')

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        node = self.keys[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.val = value
            self._move_to_head(node)
        else:
            if self.size >= self.capacity:
                self._del_tail()
            self.size += 1
            node = Node(key, value)
            self.keys[key] = node
            node.next = self.head.next
            node.next.pre = node
            node.pre = self.head
            self.head.next = node


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    print(lRUCache.get(1))
    lRUCache._print_data()
    lRUCache.put(2, 2)
    lRUCache._print_data()
    print(lRUCache.get(1))
    lRUCache._print_data()
    print(lRUCache.put(3, 3))
    print(lRUCache.get(2))
    print(lRUCache.put(4, 4))
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))