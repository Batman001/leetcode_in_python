# -*- coding:utf-8 -*-


class Solution:
    def find_duplicate(self, nums):
        """
        leetcode 287 寻找数组中重复元素 只有一个元素重复
        示例：输入: [1,3,4,2,2] 输出: 2
        示例：输入: [3,1,3,4,2] 输出: 3
        :param nums: 包含重复元素的数组
        :return: 返回重复的元素
        处理方案: 对数组排序 然后使用二分查找法进行查找重复元素
        """
        nums.sort()
        left, right = 0, len(nums)-1
        target = 0

        while left < right:
            if nums[left] == nums[left+1]:
                target = nums[left]
                break
            else:
                left += 1
            if nums[right] == nums[right-1]:
                target = nums[right]
                break
            else:
                right -= 1
        return target

    def find_duplicate_(self, nums):
        """
        leetcode 287 寻找数组中重复元素 只有一个元素重复
        :param nums: 包含重复元素的数组
        :return: 返回重复的元素
        处理方案:
        快慢指针思想 fast 和 slow 是指针, nums[slow] 表示取指针对应的元素
        注意 nums 数组中的数字都是在 1 到 n 之间的(在数组中进行游走不会越界),
        因为有重复数字的出现, 所以这个游走必然是成环的, 环的入口就是重复的元素,
        即按照寻找链表环入口的思路来做
        """
        slow, fast = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                fast = 0
                while nums[slow] != nums[fast]:
                    fast = nums[fast]
                    slow = nums[slow]

                return nums[slow]
