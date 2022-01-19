# 870. 优势洗牌
# 给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。
# 返回 A 的任意排列，使其相对于 B 的优势最大化。
# 
# 示例 1：
# 输入：A = [2,7,11,15], B = [1,10,4,11]
# 输出：[2,11,7,15]
# 
# 示例 2：
# 输入：A = [12,24,8,32], B = [13,25,32,11]
# 输出：[24,32,8,12]

# 田忌赛马的扩展版本。策略就是先排序，用自己最好的马和对方最好的马比，比得过就比，比不过就用自己最差的马送人头

class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort(reverse=True)
        res = [None for _ in range(len(nums1))]
        sorted_nums2 = [(num, i) for i, num in enumerate(nums2)]
        sorted_nums2.sort(key=lambda x : x[0], reverse=True)
        head = 0
        tail = len(nums1) - 1
        for num, index in sorted_nums2:
            if nums1[head] > num:
                res[index] = nums1[head]
                head += 1
            else:
                res[index] = nums1[tail]
                tail -= 1
        return res

if __name__ == '__main__':
    A = [2,7,11,15]
    B = [1,10,4,11]
    print(Solution().advantageCount(A, B))