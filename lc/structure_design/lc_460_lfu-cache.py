# 460. LFU 缓存
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。
# 实现 LFUCache 类：
# LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
# int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。
# void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用 的键。
# 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
# 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.key2value = {}  # key => value
        self.freq2keys = {} # freq => keys, keys 本身是 OrderedDict
        self.key2freq = {}  # key => freq
        self.capacity = capacity
        self.min_freq = 0
    
    def _delMinFreqKey(self):
        # self.freq2keys[self.min_freq] 的值是 OrderedDict，将最早加入该 dict 的 key 删除
        key, _ = self.freq2keys[self.min_freq].popitem(last=False) 
        self.key2freq.pop(key)
        self.key2value.pop(key)
        if len(self.freq2keys[self.min_freq]) == 0:
            self.freq2keys.pop(self.min_freq)

    def _increaseFreq(self, key):
        # print(f'key2freq={self.key2freq}  freq2keys={self.freq2keys}')
        freq = self.key2freq[key]
        new_freq = freq + 1
        self.key2freq[key] = new_freq
        self.freq2keys[freq].pop(key)
        if new_freq not in self.freq2keys:
            d = OrderedDict()
            d[key] = True
            self.freq2keys[new_freq] = d
        else:
            self.freq2keys[new_freq][key] = True
        if len(self.freq2keys[freq]) == 0:
            self.freq2keys.pop(freq)
            if self.min_freq == freq:
                self.min_freq = new_freq

    def get(self, key: int) -> int:
        print(f'{self.key2value}')
        if key not in self.key2value:
            return -1
        self._increaseFreq(key)
        return self.key2value[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        if key in self.key2value:
            self.key2value[key] = value
            self._increaseFreq(key)
            return

        if len(self.key2value) >= self.capacity:
            self._delMinFreqKey()
        self.key2value[key] = value
        if 1 not in self.freq2keys:
            d = OrderedDict()
            d[key] = True
            self.freq2keys[1] = d
        else:
            self.freq2keys[1][key] = True
        self.key2freq[key] = 1

        self.min_freq = 1
        return


if __name__ == '__main__':
    c = LFUCache(3)
    c.put(1, 1)
    print(f'{c.key2value}')
    c.put(2, 2)
    print(c.get(1))
    # c = LFUCache(3)
    # c.put('k1', 'v1')
    # c.put('k2', 'v2')
    # c.put('k3', 'v3')
    # c.put('k4', 'k4')
    # print(c.get('k1'))
    # print(c.get('k2'))
