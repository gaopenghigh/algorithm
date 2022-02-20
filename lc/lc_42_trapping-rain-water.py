# 42. 接雨水
# 难度 困难
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 
# 示例 2：
# 输入：height = [4,2,0,3,2,5]
# 输出：9

# 考虑格子 i，它的高度为 height[i]，找到它左边最高的柱子的高度 lMax, 再找到它右边最高的柱子的高度 rMax，
# 则这个格子能装的水为 min(lMax, rMax) - height[i]，如果是负值则能装的水为 0.
# 所以可以将每个格子左边最高的柱子高度和右边最高的柱子高度记录下来，存为 lMax[i] 和 rMax[i]
# 则格子 i 能装的水为:
# r = min(lMax[i], rMax[i]) - height[i]
# if r < 0:
#     r = 0
# 上面的方法时间复杂度为 O(n)，空间复杂度也为 O(n)
# 

class Solution:
    # 暴力解法
    # 对于格子 i，lMax 表示它左边最高的柱子，rMax 表示它右边最高的柱子，则格子 i 能接的雨水量为 max(min(l_max, r_max) - height[i], 0)
    # 而 lMax = max(height[:i]), rMax = max(height[i+1:])
    def trap(self, height: list[int]) -> int:
        r = 0
        for i in range(1, len(height)-1):
            w = max(0, min(max(height[:i]), max(height[i+1:])) - height[i])
            r += w
        return r
    
    # 实现计算出每个格子左边和右边的最高柱子的高度
    def trap2(self, height: list[int]) -> int:
        lMax = [0 for _ in range(len(height))]
        rMax = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            lMax[i] = max(lMax[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            rMax[i] = max(rMax[i+1], height[i+1])
        r = 0
        for i in range(1, len(height)-1):
            w = max(0, min(lMax[i], rMax[i]) - height[i])
            r += w
        return r
