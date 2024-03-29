# 39. 组合总和
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
# 
# 示例 1：
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
#
# 示例 2：
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
#
# 示例 3：
# 输入: candidates = [2], target = 1
# 输出: []
#
# 示例 4：
# 输入: candidates = [1], target = 1
# 输出: [[1]]
# 
# 示例 5：
# 输入: candidates = [1], target = 2
# 输出: [[1,1]]
#  
# 提示：
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都 互不相同
# 1 <= target <= 500
# 
# 链接：https://leetcode-cn.com/problems/combination-sum


# 回溯算法的框架，具体可以参考 https://labuladong.gitee.io/algo/1/4/
# result = []
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return
#     
#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 选择列表)
#         撤销选择
# 
# 本题还有如下条件：
# 1. 只考虑组合而不必考虑顺序
# 2. 通过事先将数组排序可以做一定的优化

class Solution:
    def __init__(self) -> None:
        self.result = []

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        self.backtrack(candidates, 0, [], target)
        return self.result
    
    def backtrack(self, candidates: list[int], index: int, track: list[int], target: int):
        if target < 0:
            return
        if target == 0:
            self.result.append([e for e in track])
            return
        
        # 由于已经实现排好序，我们要找的值是 <= target 的
        # 所以当 track 中的最后一个元素已经大于 target 时，再往后找已经不可能找到更小的值了
        if track and target < track[-1]:
            return
        
        # 只需要组合而不是排列，所以只需要往后看, i 从 index 开始
        for i in range(index, len(candidates)):
            num = candidates[i]
            track.append(num)
            self.backtrack(candidates, i, track, target - num)
            track.pop()


if __name__ == '__main__':
    candidates = [2,3,5]
    target = 8
    print(Solution().combinationSum(candidates, target))