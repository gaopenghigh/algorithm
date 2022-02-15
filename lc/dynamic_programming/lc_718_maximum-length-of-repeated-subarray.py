# 718. 最长重复子数组
# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。
# 
# 示例 1：
# 输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# 输出：3
# 解释：长度最长的公共子数组是 [3,2,1] 。
# 
# 示例 2：
# 输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# 输出：5


# 动态规划
# 描述一个子问题的“状态”就是两个字符串，“选择”就是两个字符串中的每 2 个字符的配对情况。
# dp[i][j] 表示以 nums1[i-1] 和 nums2[j-1] 结尾的最长重复子数组的长度，则
# if nums1[i-1] == nums2[j-1]
#     dp[i][j] = 1 + dp[i-1][j-1]
# else
#     dp(i][j] = 0
# 
# base case：
# dp[0][j] = 0
# dp[i][0] = 0


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        dp = [ [0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
        ans = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans, dp[i][j])
        return ans

if __name__ == '__main__':
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]
    nums1 = [0,0,0,0,0]
    nums2 = [0,0,0,0,0]
    print(Solution().findLength(nums1, nums2))

        