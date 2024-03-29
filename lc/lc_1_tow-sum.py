# 1. 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
# 
# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 
# 示例 2：
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 
# 示例 3：
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
# 
# 提示：
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# 只会存在一个有效答案
# 进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num in m:
                return [i, m[num]]
            want = target - num
            m[want] = i

# 如果对空间复杂度有要求，同时要求返回的不是下标而是具体的数字，就对数组先排序，然后使用双指针
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            r = nums[left] + nums[right]
            if r == target:
                return nums[left], nums[right]
            if r < target:
                left +=1
            elif r > target:
                right -= 1


if __name__ == '__main__':
    nums = [3, 2, 3]
    target = 6
    print(Solution2().twoSum(nums, target))