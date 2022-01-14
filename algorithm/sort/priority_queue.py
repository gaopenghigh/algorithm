import sys
sys.path.append('..')
import lib.util_sort as lib

class PQ(object):
    def __init__(self) -> None:
        super().__init__()
        self.arr = []
        self.length = 0

    def _sink(self, i):
        while i * 2 + 1 < self.length:
            l = i * 2 + 1
            r = i * 2 + 2
            largest = i
            if l < self.length and self.arr[largest] < self.arr[l]:
                largest = l
            if r < self.length and self.arr[largest] < self.arr[r]:
                largest = r
            if largest != i:
                self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
                i = largest
            else:
                return
    
    def _swim(self, i):
        root = (i - 1) // 2
        while root >= 0 and self.arr[root] < self.arr[i]:
            self.arr[root], self.arr[i] = self.arr[i], self.arr[root]
            i = root
            root = (i - 1) // 2
    
    def add(self, i):
        self.arr.append(i)
        self.length += 1
        self._swim(self.length -1)
    
    def pop(self):
        larget = self.arr[0]
        self.arr[0], self.arr[self.length - 1] = self.arr[self.length - 1], self.arr[0]
        self.length -= 1
        self._sink(0)
        return larget

@lib.print_spend_time
def test_pq(n):
    arr = lib.get_random_array(n)
    pq = PQ()
    for i in arr:
        pq.add(i)
    lib.print_array(pq.arr)
    while pq.length > 0:
        r = pq.pop()
        print(r)

if __name__ == "__main__":
    test_pq(8)
