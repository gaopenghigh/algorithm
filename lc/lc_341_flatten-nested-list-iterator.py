# 341. 扁平化嵌套列表迭代器
# 给你一个嵌套的整数列表 nestedList 。每个元素要么是一个整数，要么是一个列表；该列表的元素也可能是整数或者是其他列表。请你实现一个迭代器将其扁平化，使之能够遍历这个列表中的所有整数。

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> list:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """

class NestedIterator:
    def __init__(self, nestedList: list):
        self.data = nestedList[:]
    
    def next(self) -> int:
        return self.data.pop(0)
    
    def hasNext(self) -> bool:
        if len(self.data) == 0:
            return False
        d = self.data.pop(0)
        if not d.isInteger():
            self.data = d.getList() + self.data
            return self.hasNext()
        self.data = [d] + self.data
        return True
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())