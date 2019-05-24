# -*- coding:utf-8 -*-
def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    i, sum_, length = 0, 0, 0
    for j in range(len(nums)):
        sum_ += nums[j]
        while sum_ >= s:
            length = j-i+1 if length == 0 else min(length, j-i+1)
            i += 1
            sum_ -= nums[i]
    return length


if __name__ == "__main__":
    s = 4
    nums = [1, 4, 4]
    print(minSubArrayLen(s, nums))



