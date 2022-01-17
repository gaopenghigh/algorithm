# 496. 下一个更大元素 I
# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

# 所有”下一个最大“之类的题目，都使用单调栈解决。
# 所谓单调栈，就是栈中下面的元素肯定比上面的元素大。可以想象往栈里面压入元素时，上面的元素会把下面比它小的元素都压扁掉，知道遇到比它大的元素。

# 对于本题，我们需要先找到 nums 中所有元素对应的它后面比它大的第一个元素。将结果记录在一个 map 中，然后再遍历 nums1，从 map 中找到答案。
# 从后往前遍历元素压栈，压入一个元素后，最终在它下面的元素，就是它身后第一个比它大的元素了。

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m = {}
        stack = []
        for i in reversed(nums2):
            while stack and stack[-1] < i:
                stack.pop()
            m[i] = stack[-1] if len(stack) > 0 else -1
            stack.append(i)
        return [m[i] for i in nums1]
