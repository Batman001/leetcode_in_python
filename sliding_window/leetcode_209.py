# -*- coding:utf-8 -*-
class Solution:

    @staticmethod
    def min_subarray_len(s, nums):
        """
        https://leetcode-cn.com/problems/minimum-size-subarray-sum/
        给定一个含有 n 个正整数的数组和一个正整数 s ，
        找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
        如果不存在符合条件的连续子数组，返回 0
        :param s:
        :param nums:
        :return:
        """

        # 滑动窗口范围
        left, right = 0, -1

        # 辅助变量
        window_sum = 0
        min_len = None

        # 终止条件
        while left < len(nums):

            # 滑动条件
            if window_sum < s and right + 1 < len(nums):
                window_sum += nums[right + 1]
                right += 1
            else:
                window_sum -= nums[left]
                left += 1

            # 改变结果
            if window_sum >= s:
                min_len = min(min_len, right - left + 1) if min_len is not None else right - left + 1
        # 返回结果
        return min_len if min_len is not None else 0



