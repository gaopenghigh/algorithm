# 486. 预测赢家
# 给你一个整数数组 nums 。玩家 1 和玩家 2 基于这个数组设计了一个游戏。
# 玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手。开始时，两个玩家的初始分值都是 0 。每一回合，玩家从数组的任意一端取一个数字（即，nums[0] 或 nums[nums.length - 1]），取到的数字将会从数组中移除（数组长度减 1 ）。玩家选中的数字将会加到他的得分上。当数组中没有剩余数字可取时，游戏结束。
# 如果玩家 1 能成为赢家，返回 true 。如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 true 。你可以假设每个玩家的玩法都会使他的分数最大化。
# 
# 示例 1：
# 输入：nums = [1,5,2]
# 输出：false
# 解释：一开始，玩家 1 可以从 1 和 2 中进行选择。
# 如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。 
# 所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
# 因此，玩家 1 永远不会成为赢家，返回 false 。
# 
# 示例 2：
# 输入：nums = [1,5,233,7]
# 输出：true
# 解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
# 最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 true，表示玩家 1 可以成为赢家。

# 对于 nums[i:j] 我们想算出先手能得到的最高分数和后手能得到的最高分数，分别记为 first(nums[i:j]) 和 second(nums[i:j])
# 对于先手，可以选择左边 nums[i] 或者右边 nums[j-1]
#    如果选择左边 nums[i]，则下一次轮到自己选，变成了 nums[i+1:j] 的后手的最高分，也就是 second(nums[i+1:j])，得分为 nums[i] + second(nums[i+1:j]
#        此时后手的得分就是 first(nums[i+1:j])
#    如果选择右边 nums[j-1]，则下一次轮到自己选，就变成了 nums[i:j-1] 的后手的最高分，也就是 second(nums[i:j-1])，得分为 nums[j-1] + second(nums[i:j-1])
#        此时后手得分就是 first(nums[i:j-1])
# 总结下来就是：
# first(nums[i:j]) = max( nums[i] + second(nums[i+1:j]),  nums[j-1] + second(nums[i:j-1]) )
# second(nums[i:j]) = if 先手选择左边
#                         first(nums[i+1:j])
#                     lese
#                         first(nums[i:j-1])
# base case: 当 i==j-1（python 中的截取） 时，就只有一堆数字，显然先手必胜，first(nums[x:x]) = nums[x], second(nums[x:x]) = 0
# 至此可以写出递归方法，最后再加上优化重复计算的 cache

class Solution:
    def __init__(self) -> None:
        self.nums = None
        self.length = 0
        self.first_cache = {}
        self.second_cache = {}

    def PredictTheWinner(self, nums: list[int]) -> bool:
        self.nums = nums
        self.length = len(nums)
        first = self.first(0, self.length)
        second = self.second(0, self.length)
        # print(f'first score = {first}, second score = {second}')
        return first >= second
    
    def first(self, i, j):
        if i == j-1:
            return self.nums[i]
        if (i, j) in self.first_cache:
            return self.first_cache[(i, j)]
        score_left = self.nums[i] + self.second(i+1, j)
        score_right = self.nums[j-1] + self.second(i, j-1)
        score = max(score_left, score_right)
        self.first_cache[(i, j)] = score
        return score

    def second(self, i, j):
        if i == j-1:
            return 0
        if (i, j) in self.second_cache:
            return self.second_cache[(i, j)]
        first_score_left = self.nums[i] + self.second(i+1, j)
        first_score_right = self.nums[j-1] + self.second(i, j-1)
        score = None
        if first_score_left > first_score_right:
            score = self.first(i+1, j)
        else:
            score = self.first(i, j-1)
        self.second_cache[(i, j)] = score
        return score


if __name__ == '__main__':
    s = Solution()
    nums = [1,5,2]
    nums = [1,5,233,7]
    print(s.PredictTheWinner(nums))
 