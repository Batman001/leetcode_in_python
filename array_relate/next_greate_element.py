# -*- coding:utf-8 -*-
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [-1 for _ in range(len(nums1))]
        for i in range(len(nums1)):
            next_larger_num = self.next_greate_ele_(nums1[i], nums2)
            res[i] = next_larger_num
        return res

    def next_greate_ele_(self, cur_num, nums):
        target = -1
        cur_index = nums.index(cur_num)
        for i in range(cur_index+1, len(nums)):
            if nums[i] > cur_num:
                target = nums[i]
                break
        return target


if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 2, 3, 4]
    s = Solution()
    res = s.nextGreaterElement(nums1, nums2)
    print(res)

