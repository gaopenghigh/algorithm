# 295. 数据流的中位数
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
# 例如，
# [2,3,4] 的中位数是 3
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 设计一个支持以下两种操作的数据结构：
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。

# 想象两个口袋，左边一个右边一个，数字从流中流出，然后左边放一个，右边放一个，
# 保证左边口袋和右边口袋数字个数一样，或者左边比右边多一个。
# 然后想办法保证左边口袋中的数字都 <= 右边口袋中的数字
# 如果左右两个口袋中的数字个数一样，则从分别找到左边口袋的最大值和右边口袋的最小值，其平均值就是中位数。
# 如果不一样，那肯定只能是左边口袋中的数字比右边口袋中的数字多一个，那左边口袋中的最大值就是中位数。
# 所以关键点就是怎么保证左边口袋中的数 <= 右边口袋中的数。
# 如果轮到左边口袋中增加数字，不能直接放到左边，因为由于新拿到的数字很可能比较大，本应该放在右边的，
# 我们可以先把数字放右边，然后从右边口袋中挑出最小的一个数字，放到左边去。这样右边数字个数不会增加，但左边增加了一个。
# 同理，如果轮到右边口袋增加数字，先把新的数字放左边，然后从左边中挑出最大的一个来放到右边即可。
# 左边口袋可以用大根堆，右边口袋可以用小根堆。

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class MedianFinder:

    def __init__(self):
        self.left = MaxHeap()
        self.right = MinHeap()
        self.leftOrder = True

    def addNum(self, num: int) -> None:
        if self.leftOrder:
            self.right.push(num)
            self.left.push(self.right.pop())
        else:
            self.left.push(num)
            self.right.push(self.left.pop())
        self.leftOrder = not self.leftOrder

    def findMedian(self) -> float:
        if self.leftOrder: # 左右个数一致
            return (self.left.top() + self.right.top()) / 2.0
        else:
            return self.left.top()


class MinHeap:
    def __init__(self) -> None:
        self.data = []
    
    def _swim(self, i):
        while (i - 1) // 2 >= 0:
            parent = (i-1)//2
            if self.data[parent] > self.data[i]:
                self.data[parent], self.data[i] = self.data[i], self.data[parent]
                i = parent
            else:
                break

    def _sink(self, i):
        n = len(self.data)
        while i * 2 + 1 <= n - 1:
            smallest = i
            left = i * 2 + 1
            right = i * 2 + 2
            if left <= n - 1 and self.data[left] < self.data[smallest]:
                smallest = left
            if right <= n - 1 and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest != i:
                self.data[smallest], self.data[i] = self.data[i], self.data[smallest]
                i = smallest
            else:
                break
    
    def pop(self):
        r = self.data[0]
        n = len(self.data)
        self.data[0], self.data[n-1] = self.data[n-1], self.data[0]
        self.data.pop()
        self._sink(0)
        return r

    def top(self):
        return self.data[0]
    
    def push(self, v):
        self.data.append(v)
        self._swim(len(self.data) - 1)

class MaxHeap:
    def __init__(self) -> None:
        self.data = []
    
    def _swim(self, i):
        while (i - 1) // 2 >= 0:
            parent = (i-1)//2
            if self.data[parent] < self.data[i]:
                self.data[parent], self.data[i] = self.data[i], self.data[parent]
                i = parent
            else:
                break

    def _sink(self, i):
        n = len(self.data)
        while i * 2 + 1 <= n - 1:
            biggest = i
            left = i * 2 + 1
            right = i * 2 + 2
            if left <= n - 1 and self.data[left] > self.data[biggest]:
                biggest = left
            if right <= n - 1 and self.data[right] > self.data[biggest]:
                biggest = right
            if biggest != i:
                self.data[biggest], self.data[i] = self.data[i], self.data[biggest]
                i = biggest
            else:
                break
    
    def pop(self):
        r = self.data[0]
        n = len(self.data)
        self.data[0], self.data[n-1] = self.data[n-1], self.data[0]
        self.data.pop()
        self._sink(0)
        return r

    def top(self):
        return self.data[0]
    
    def push(self, v):
        self.data.append(v)
        self._swim(len(self.data) - 1)
    


if __name__ == '__main__':
    f = MedianFinder()
    f.addNum(3)
    f.addNum(1)
    f.addNum(2)
    print(f.findMedian())