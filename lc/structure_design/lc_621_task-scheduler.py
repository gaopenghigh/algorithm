# 621. 任务调度器
# 难度 中等
# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
# 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
# 你需要计算完成所有任务所需要的 最短时间 。
# 
# 示例 1：
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
#      在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
# 
# 示例 2：
# 输入：tasks = ["A","A","A","B","B","B"], n = 0
# 输出：6
# 解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# 诸如此类
# 
# 示例 3：
# 输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# 输出：16
# 解释：一种可能的解决方案是：
#      A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A


# 直观的思路
# 首先统计每种任务需要执行的次数
# 每一个时钟周期，从中挑出剩余次数最多并且没有在冷却过程中的那个任务去执行

class Solution:
    def __init__(self) -> None:
        self.taskMap = {}
        self.interval = 0
        self.totalTasks = 0

    def leastInterval(self, tasks: list[str], n: int) -> int:
        self.interval = n
        for t in tasks:
            self.totalTasks += 1
            if t not in self.taskMap:
                self.taskMap[t] = TaskInfo()
            else:
                ti = self.taskMap[t]
                ti.count = ti.count + 1
                self.taskMap[t] = ti
        i = 1
        while self.totalTasks > 0:
            t = self.pick(i)
            i += 1
        return i - 1

    def pick(self, i):
        maxCount = 0
        taskName = None
        taskInfo = None
        for name, ti in self.taskMap.items():
            if ti.nextValid <= i and ti.count > maxCount:
                maxCount = ti.count
                taskName = name
        if not taskName:
            return None
        self.totalTasks -= 1
        taskInfo = self.taskMap[taskName]
        taskInfo.count -= 1
        taskInfo.nextValid = i + self.interval + 1
        if taskInfo.count == 0:
            self.taskMap.pop(taskName)
        else:
            self.taskMap[taskName] = taskInfo
        return taskName


class TaskInfo:
    def __init__(self, count=1, nextValid=1) -> None:
        self.count = count
        self.nextValid = nextValid


if __name__ == '__main__':
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    print(Solution().leastInterval(tasks, n))