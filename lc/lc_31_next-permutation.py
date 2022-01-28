# 31. 下一个排列
# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
# 
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
# 
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。

# 最大的排列肯定是从左到右逐渐变小的，比如 5,4,3,2,1，此时下一个排列就是翻转这个数组变成 1,2,3,4,5。
# 而对于一般情况，下一个排列肯定是从右开始向左看，看看能动哪一位。比如 1,3,5,4,2，如果以 1,3 开头，由于后面的 5,4,2 以及是最大排列，没什么可动的，所以只能动 3 。
# 开头的 1 保持不变，3 就需要和后面的 5,4,2 中的一个作为交换。由于需要得到的是“下一个”排列，所以我们需要从 5,4,2 中找到刚刚比 3 大的那个数。而又由于 5,4,2 以及是从大到小的，所以只需要从右往左找第一个比 3 大的树，也就是 4，把它和 3 交换，得到 1,4,5,3,2。
# 这时仍然不是“下一个”排列。因为从 1,3,5,4,2 变成 1,4,5,3,2 后，左边第二位已经变高了，所有右面的位置应该尽可能地小，也就是 5,3,2 应该变成 2,3,5。而同样由于后面几位是非递增的，所有只需要翻转一下就好了。

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 2:
            nums.reverse()
            return
        # 从右往左，看到哪一位开始从非递减变成了递减
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        # 如果整个数组已经是递减的，说明已经到了最大的那个排列，翻转即可
        if i == -1:
            nums.reverse()
            return
        # 在 nums[i+1:] 中，从右到左，找到第一个比 nums[i] 大的数字
        j = len(nums) - 1
        while j >= i+1:
            if nums[j] > nums[i]:
                break
            j -= 1
        # 交换
        nums[i], nums[j] = nums[j], nums[i]
        # 将 nums[i+1:] 翻转
        left = i+1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    nums = [1, 2, 3]
    nums = [3, 2, 1]
    nums  = [1, 2]
    Solution().nextPermutation(nums)
    print(nums)