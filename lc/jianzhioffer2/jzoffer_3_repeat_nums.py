# 找出数组中重复的数字。

# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
# 
# 示例 1：
# 
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3 
# 
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof

# 最直观的方法就是使用一个 map 存储出现过的数字
# 一个优化的方式是利用“长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内”的条件，使用 index 来标记出现过的数字。

class Solution:
    def findRepeatNumber(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            curr_val = nums[i]
            if curr_val >= n:
                curr_val = curr_val - n
            marker_pos_val = nums[curr_val]
            # this val is already been marked before
            if marker_pos_val >= n:
                return curr_val
            # mark val in position curr_val
            nums[curr_val] = nums[curr_val] + n


def test():
    arr = [3, 4, 2, 0, 0, 1]
    s = Solution()
    print(s.findRepeatNumber(arr))

if __name__ == '__main__':
    test()