# -*- coding:utf-8 -*-


def find_unsorted_subarray(nums):
    """
    581. 最短无序连续子数组 https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/
    给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
    solution https://www.cnblogs.com/jimmycheng/p/7673733.html
    :param nums: list[int]
    :return: int
    input [2, 6, 4, 8, 10, 9, 15]
    output 5

    """
    length = len(nums)
    min_num = nums[-1]
    max_num = nums[0]
    end = -2
    beg = -1
    for i in range(0, length):
        # max_num from right to left
        max_num = max(max_num, nums[i])
        # min_num from left to right
        min_num = min(min_num, nums[length-1-i])
        if nums[i] < max_num:
            end = i
        if nums[length-1-i] > min_num:
            beg = length - 1 - i

    return end - beg + 1


if __name__ == "__main__":
    nums = [2, 6, 4, 8, 10, 9, 15]
    result = find_unsorted_subarray(nums)
    print(result)
