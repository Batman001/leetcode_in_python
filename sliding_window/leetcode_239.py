# -*- coding:utf-8 -*-
from collections import deque


class Solution(object):

    @staticmethod
    def max_sliding_window(self, nums, k):
        """
        时间复杂度为 O(k*n-k)
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        if nums == [] or k == 0:
            return result
        if k == 1:
            return nums
        left, right = 0, 0
        while right < len(nums) and left <= len(nums) - k:
            cur_max_num = nums[left]
            while right - left + 1 <= k:
                if nums[right] > cur_max_num:
                    cur_max_num = nums[right]
                    # print("current_max_num " + str(cur_max_num))
                right += 1
            result.append(cur_max_num)
            left += 1
            right = left + 1
        return result

    @staticmethod
    def max_sliding_window_(self, nums, k):
        """
        wrong code 如果最大值出现中间 没有办法处理
        max_sliding_window_([1,3,1,2,0,5], 3) 打印结果为: [3,3,1,5] 正确答案为[3,3,2,5]
        :param nums:
        :param k:
        :return:
        """
        result = []
        if nums == [] or k == 0:
            return result
        if k == 1:
            return nums
        cur_max_num = max(nums[0:k])
        result.append(cur_max_num)
        for i in range(1, len(nums)-k+1):
            # 不包含前面left指针的元素值最大的情形
            if cur_max_num == nums[i-1]:
                cur_max_num = 0
            cur_max_num = max(cur_max_num, nums[i], nums[i+k-1])
            result.append(cur_max_num)
        return result

    @staticmethod
    def max_sliding_window1(self, nums, k):
        """
        使用辅助队列数据结构实现
        :param nums:
        :param k:
        :return:
        """
        q = deque()
        max_window = []

        for i, num in enumerate(nums):

            while q and nums[q[-1]] < num:
                q.pop()

            q.append(i)

            if q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                max_window.append(nums[q[0]])

        return max_window


if __name__ == "__main__":
    s = Solution()
    nums_ = [1, 3, -1, -3, 5, 3, 6, 7]
    k_ = 3
    result = s.max_sliding_window1(nums_, k_)