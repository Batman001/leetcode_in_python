# -*- coding:utf-8 -*-
# LeetCode 88: 合并两个有序数组


def merge(nums1, m, nums2, n):
    """
    给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中
    :param nums1: 第一个有序数组，有足够空间
    :param m: nums1有效元素个数
    :param nums2: 第二个有序数组
    :param n: nums2有效元素个数
    :return: 合并后的nums1
    """
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1

    nums1[:j + 1] = nums2[:j + 1]
    return nums1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 4, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print("合并结果:", nums1)