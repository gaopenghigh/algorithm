# 698. 划分为k个相等的子集
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 示例 1：
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。

# 回溯算法做选择时，尽可能地让每次可选的少一点，宁可选择的次数多一点。而不是每次从很多个选择中选一个。
# 也即是让选择树变得瘦长，好过变得扁宽
# k 个子集想象为 k 个桶，我们一个桶一个桶地装，把一个桶刚好装到 target 就下一个桶。

class Solution:
    def __init__(self) -> None:
         self.nums = None
         self.target = None
         self.buckets = None
         self.used = {}

    # 我们一个桶一个桶地回溯
    # 回溯第 bucketIndex 个桶，当前该桶中数字总和为 sumCurrBucket，可以从 nums[startFrom:] 中选择数字
    def backtrack(self, bucketIndex, sumCurrBucket, startFrom):
        # 回溯到最后一个桶，由于 target = total / k, 所以剩下的数字肯定刚好和为 target
        if bucketIndex == self.buckets - 1:
            return True
        # 当前桶正好装满了，开始装下一个，并且可以从 nums[0:] 中选择数字
        if sumCurrBucket == self.target:
            return self.backtrack(bucketIndex+1, 0, 0)
        for i in range(startFrom, len(self.nums)):
            # 已经装到其他桶了
            if self.used[i]:
                continue
            # 这个数太大了，现在不可能，今后也不可能装进当前桶了
            if sumCurrBucket + self.nums[i] > self.target:
                continue
            # 把当前数字装入当前桶，然后继续递归看下一个数字，下次递归中，数字可以直接从 i+1 位置开始选
            # 因为之前的数字，要么被已经装进某个桶了，要么太大了不能放进当前桶
            sumCurrBucket += self.nums[i]
            self.used[i] = True
            if self.backtrack(bucketIndex, sumCurrBucket, i+1):
                return True
            # 取出来
            sumCurrBucket -= self.nums[i]
            self.used[i] = False
        return False

    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        if len(nums) < k:
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        self.nums = nums
        self.target = target
        self.buckets = k
        self.used = {i : False for i in range(len(nums))}
        return self.backtrack(0, 0, 0)


if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(Solution().canPartitionKSubsets(nums, k))