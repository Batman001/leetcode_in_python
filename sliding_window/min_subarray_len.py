# -*- coding:utf-8 -*-
class Solution:

    def __init__(self, target, nums):
        """
        初始化函数
        :param target: 满足条件的子数组的和
        :param nums: 数组
        """
        self.target = target
        self.nums = nums

    def min_subarray_len(self):
        """
        leetcode 长度最小的数组(使用窗口算法 或者双指针)
        :return: 子数组的长度
        """
        left, sum_, length = 0, 0, len(self.nums)
        res = length + 1
        for i in range(length):
            sum_ += nums[i]
            if sum_ >= self.target:
                while sum_ - nums[left] >= self.target:
                    sum_ -= nums[left]
                    left += 1
                res = min(res, i - left + 1)

        if res == length + 1:
            return 0
        else:
            return res


if __name__ == "__main__":
    target = 4
    nums = [1, 4, 4]
    s = Solution(target, nums)

    print(s.min_subarray_len())



