# 34. 在排序数组中查找元素的第一个和最后一个位置
# 难度 中等
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 进阶：
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
# 
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 
# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 
# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]


# 两次使用二分法求出左边界和右边界

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        leftIndex = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        rightIndex = right
        return [leftIndex, rightIndex]


if __name__ == '__main__':
    # 输入：nums = [5,7,7,8,8,10], target = 8
    # 输出：[3,4]
    nums = [5,7,7,8,8,10]
    nums = [2,2]
    target = 3
    print(Solution().searchRange(nums, target))
