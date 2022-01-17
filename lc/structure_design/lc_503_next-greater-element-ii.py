# 503. 下一个更大元素 II
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

# 使用单调栈，循环数组的技巧是将数组复制一份接到原来的数组后面，优化的技巧是索引值取余。

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        m = [None for _ in range(len(nums))]
        stack = []
        # 假装数组长度翻倍
        i = 2 * n -1
        while i >= 0:
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            m[i%n] = stack[-1] if stack else -1
            stack.append(nums[i%n])
            i -= 1
        return m


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,1]
    print(s.nextGreaterElements(nums))