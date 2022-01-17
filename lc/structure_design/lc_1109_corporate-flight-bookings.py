# 1109. 航班预订统计
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
# 请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。

# 针对批量对某一区间的元素做某个同样加减操作的情况，使用差分数组记录所做的变化。

class DiffArray:
    def __init__(self, arr) -> None:
        self.diff = [arr[0]]
        for i in range(1, len(arr)):
            self.diff.append(arr[i] - arr[i-1])
    
    def result(self):
        res = [self.diff[0]]
        for i in range(1, len(self.diff)):
            res.append(res[i-1] + self.diff[i])
        return res
    
    def increase(self, start, end, val):
        self.diff[start] += val
        if end + 1 <= len(self.diff) - 1:
            self.diff[end+1] -= val

    def decrease(self, start, end, val):
        self.increase(start, end, 0 - val)


class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        flights = [0 for _ in range(n)]
        diff = DiffArray(flights)
        for b in bookings:
            start, end, seats = b[0] - 1, b[1] - 1, b[2]
            diff.increase(start, end, seats)
        return diff.result()


if __name__ == '__main__':
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    print(Solution().corpFlightBookings(bookings, n))