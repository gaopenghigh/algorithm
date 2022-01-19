# 380. O(1) 时间插入、删除和获取随机元素
# 实现RandomizedSet 类：
# RandomizedSet() 初始化 RandomizedSet 对象
# bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
# bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
# int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
# 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

# 使用 map 和 list 的组合，map 中存 val 到 array 索引的映射关系
# 注意，hashmap 的时间复杂度为 O(1)
# 从 arr 中删除索引 i 的元素时，可以把它与最后一个元素交换，然后删除最后一个元素

import random

class RandomizedSet:

    def __init__(self):
        self.m = {}
        self.arr =[]

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        self.arr.append(val)
        self.m[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        index = self.m[val]
        last_val = self.arr[-1]
        self.m[last_val] = index
        self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
        self.arr.pop()
        self.m.pop(val)
        return True

    def getRandom(self) -> int:
        rand_index = random.randint(0, len(self.arr) -1)
        return self.arr[rand_index]


if __name__ == '__main__':
    o = RandomizedSet()
    print(o.insert(0))
    print(o.insert(0))
    print(o.getRandom())
    print(o.remove(0))
    print(o.insert(0))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()