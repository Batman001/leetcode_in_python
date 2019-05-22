# -*- coding:utf-8 -*-
class Solution:

    def min_subarray_len(self, s, nums):
        """
        leetcode 长度最小的数组(使用窗口算法 或者双指针)
        :param s: 满足条件的子数组的和
        :param nums: 数组
        :return: 子数组的长度
        """
        left, sum_, length = 0, 0, len(nums)
        res = length + 1
        for i in range(length):
            sum_ += nums[i]
            if sum_ >= s:
                while sum_ - nums[left] >= s:
                    sum_ -= nums[left]
                    left += 1
                res = min(res, i - left + 1)

        if res == length + 1:
            return 0
        else:
            return res


if __name__ == "__main__":
    s = Solution()
    target = 4
    nums = [1, 4, 4]
    print(s.min_subarray_len(target, nums))



