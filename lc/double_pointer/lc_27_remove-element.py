# 27. 移除元素
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

# 和最后一个元素交换然后删除

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                nums.pop()
                right -= 1
            else:
                left += 1
        return len(nums)

if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    print(Solution().removeElement(nums, val))
    print(nums)