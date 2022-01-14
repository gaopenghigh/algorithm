# 895. 最大频率栈
# 实现 FreqStack，模拟类似栈的数据结构的操作的一个类。
# FreqStack 有两个函数：
# push(int x)，将整数 x 推入栈中。
# pop()，它移除并返回栈中出现最频繁的元素。
# 如果最频繁的元素不只一个，则移除并返回最接近栈顶的元素。

# 需要领悟到一点，一个元素加入到栈中后，但就这个元素本身，它的频率是不会变得。假如添加了元素 a，其频率为 1，之后某个时候又添加了一次 a，第二个 a 的频率就是 2，而第一个 a 的频率还是 1。因为第二个 a 肯定比第一个 a 先弹出栈，所以弹到第一个 a 时，它的 频率仍旧是 1。 
# 所以关键就是为每个频率维护一个栈，里面放着该频率的元素。

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

class FreqStack:
    def __init__(self):
        self.freq2val = {}
        self.val2freq = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.val2freq.get(val, 0)
        new_freq = freq + 1
        self.val2freq[val] = new_freq
        if new_freq not in self.freq2val:
            self.freq2val[new_freq] = [val]
        else:
            self.freq2val[new_freq].append(val)
        if new_freq > self.max_freq:
            self.max_freq = new_freq

    def pop(self) -> int:
        r = self.freq2val[self.max_freq].pop()
        if len(self.freq2val[self.max_freq]) == 0:
            self.freq2val.pop(self.max_freq)
            self.max_freq -= 1
        self.val2freq[r] -= 1
        return r


# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
if __name__ == '__main__':
    s = FreqStack()
    s.push(5)
    s.push(7)
    s.push(5)
    s.push(7)
    s.push(4)
    s.push(5)
    print(f'max_freq={s.max_freq}, freq2val={s.freq2val}, val2freq={s.val2freq}')
    print(s.pop())
    print(f'max_freq={s.max_freq}, freq2val={s.freq2val}, val2freq={s.val2freq}')
    print(s.pop())
    print(f'max_freq={s.max_freq}, freq2val={s.freq2val}, val2freq={s.val2freq}')
    print(s.pop())
    print(f'max_freq={s.max_freq}, freq2val={s.freq2val}, val2freq={s.val2freq}')
    print(s.pop())
    print(f'max_freq={s.max_freq}, freq2val={s.freq2val}, val2freq={s.val2freq}')
    print(s.pop())
    print(f'max_freq={s.max_freq}, freq2val={s.freq2val}, val2freq={s.val2freq}')
