# 96. 不同的二叉搜索树
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。


# 使用递归的方法
# 随便选择一个数作为 root，则总的不同 BST 的个数，就是左边不同 BST 的个数，乘以右边不同 BST 的个数。
# 由于 n 个节点的值为 1 到 n，可以想象从小到大逐个选择节点作为 root，则左子树肯定由小于它的节点组成，右子树由大于它的节点组成。
# 由于存在重复计算，可以优化加上缓存
class Solution:
    def __init__(self) -> None:
        self.memo = {}        

    def numTrees(self, n: int) -> int:
        return self.count(1, n)

    # 计算从 low 到 high 的节点能组成多少不同的 BST
    def count(self, low, high):
        if low >= high:
            return 1
        
        if (low, high) in self.memo:
            return self.memo[(low, high)]

        totalCount = 0
        i = low
        while i <= high:
            # print(f'i={i}, low={low}, high={high}')
            leftCount = self.count(low, i - 1)
            rightCount = self.count(i + 1, high)
            currentCount = leftCount * rightCount
            totalCount += currentCount
            i += 1
        self.memo[(low, high)] = totalCount
        return totalCount


# 另外一种思路
# 随便选择一个数作为 root，则总的不同 BST 的个数，就是左边不同 BST 的个数，乘以右边不同 BST 的个数。
# 由于 n 个节点的值为 1 到 n，可以想象从小到大逐个选择节点作为 root，则左子树肯定由小于它的节点组成，右子树由大于它的节点组成。
# 而我们最终需要的结果是“个数”，所以从 1 到 5 的节点组成的不同 BST 的个数，和从 6 到 10 的节点组成的不同 BST 个数一致。
# 也就是说在节点 1 到 n 各不相同的前提下，不同 BST 个数，仅仅和节点个数有关系，而和具体是哪些节点没关系。

# 对于节点 i，其左边节点是 [1, (i-1)]，一共有 i-1 个节点，右边节点是 [(i+1), n]，一共有 n-i 个节点，所以有：
# 假设：
#   G(n): 长度为 n 的序列能构成的不同二叉搜索树的个数。
#   F(i,n): 以 i 为根、序列长度为 n 的不同二叉搜索树个数 
# 则：
# F(i, n) = G(i-1) * G(n-i)
# G(n) = SUM(F(i,n) for i in [1, n])
# 这就变成了动态规划问题，其中 base case为：
# G(0) = 1
# G(1) = 1

class Solution2:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        G = [0] * (n + 1)
        G[0] = 1
        G[1] = 1
        i = 2
        for i in range(2, n + 1):
            sumFi = 0
            for j in range(1, i+1):
                sumFi += G[j-1] * G[i-j]
            G[i] = sumFi
        return G[n]


if __name__ == '__main__':
    print(Solution().numTrees(4))