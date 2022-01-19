# 875. 爱吃香蕉的珂珂
# 珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。
# 珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  
# 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
# 返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。
# 
# 示例 1：
# 输入: piles = [3,6,7,11], H = 8
# 输出: 4
# 
# 示例 2：
# 输入: piles = [30,11,23,4,20], H = 5
# 输出: 30
# 
# 示例 3：
# 输入: piles = [30,11,23,4,20], H = 6
# 输出: 23

# 单调函数搜索的问题，可以抽象成二分查找
# 注意固定使用左开右闭区间，[left，right)

class Solution:
    def __init__(self) -> None:
        self.piles = []

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        self.piles = piles
        left = 1
        right = max(piles)
        while left < right:
            mid = left + int((right - left) / 2)
            hours = self.f(mid)
            if hours == h:
                right = mid
            elif hours > h:
                left = mid + 1
            else:
                right = mid
        return left

    # k 是吃香蕉的速度， f(k) 表示按照这个速度需要多少小时能吃完所有香蕉
    # 显然 f(k) 随着 k 的增大单调递减
    # k 最小值为 1，最大值为 piles 元素的最大值，也就是最大一堆香蕉的香蕉个数
    def f(self, k):
        hours = 0
        for p in self.piles:
            hour = int(p/k)
            if p % k > 0:
                hour += 1
            hours += hour
        return hours
            


if __name__ == '__main__':
    # piles = [3,6,7,11]
    # H = 8
    # print(Solution().minEatingSpeed(piles,H))

    # piles = [30,11,23,4,20]
    # H = 5
    # print(Solution().minEatingSpeed(piles,H))

    piles = [30,11,23,4,20]
    H = 6
    print(Solution().minEatingSpeed(piles,H))