# 55. 跳跃游戏
# 难度 中等
# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标。
# 
# 示例 1：
# nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 
# 示例 2：
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。


# 从下标 i，可以到达 nums[i:i+nums[i]] 的位置
# 注意一个事实，如果能到达某个下标，则该下标之前的所有数字都是可以到达的。
# 所以我们只需要从左到右遍历，看能到达的最大位置是否大于最后一个下标


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # right 记录最远能到达的下标
        right = 0
        i = 0
        while i < len(nums) and i <= right:
            if i + nums[i] > right:
                right = i + nums[i]
            if right >= len(nums) - 1:
                return True
            i += 1
        return False

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))