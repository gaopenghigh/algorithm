# 303. 区域和检索 - 数组不可变
# 给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
# 实现 NumArray 类：
# NumArray(int[] nums) 使用数组 nums 初始化对象
# int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# 构造前缀和查找表，计算 sum(list[0:i]) - sum(list[0:j]) 的结果
# 注意前缀和查找表的长度需要比 nums 长一位，这样能简化计算和判断，pre[i] 表示位置位于 [0, i-1] 之间元素的和

class NumArray:

    def __init__(self, nums: list[int]):
        self.pre = [0]
        i = 1
        for i in range(1, len(nums) + 1):
            self.pre.append(self.pre[i-1] + nums[i-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]


if __name__ == '__main__':
    nums = [-2,0,3,-5,2,-1]
    left = 0
    right = 2
    print(NumArray(nums).sumRange(left, right))