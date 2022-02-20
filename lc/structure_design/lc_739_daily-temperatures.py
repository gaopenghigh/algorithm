# 739. 每日温度
# 难度 中等
# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
# 其中 answer[i] 是指在第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
# 
# 示例 1:
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
# 
# 示例 2:
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
# 
# 示例 3:
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]


# 使用单调栈

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        stack = []
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < t:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans