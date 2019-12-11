# -*- coding:utf-8 -*-


def two_sum(nums, target):
    """
    在nums中找到两个数字的和为target的组合
    :param nums: 数组
    :param target: 求和目标
    :return: 满足条件的一组数
    """
    nums.sort()
    left = 0
    right = len(nums) - 1
    result = []

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            result.append([nums[left], nums[right]])
            # 处理出现重复数字的情形
            while left < right and nums[left] == nums[left + 1]:
                left += 1

            while left < right and nums[right] == nums[right - 1]:
                right -= 1
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    return result


def three_sum(nums, target):
    """
    3sum
    :param nums: 数组
    :param target: 求和目标
    :return:
    """
    nums.sort()
    result = []

    for i in range(len(nums)-2):
        first_num = nums[i]
        # 跳过第一个数字重复的情况
        if i == 0 or first_num != nums[i-1]:
            left = i + 1
            right = len(nums) - 1
            two_sum_target = target - first_num

            while left < right:
                two_sum_temp = nums[left] + nums[right]
                if two_sum_temp == two_sum_target:
                    result.append([first_num, nums[left], nums[right]])

                    # skip the duplicated nums[left]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # skip the duplicated nums[right]
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 继续向后探索(如果找到满足条件的 同时移动左指针和右指针)
                    left += 1
                    right -= 1

                # 如果现在两个值大于two_sum_target
                elif two_sum_temp > two_sum_target:
                    right -= 1
                else:
                    left += 1

    return result


if __name__ == "__main__":
    nums = [-5, -2, -4, -2, -5, -4, 0, 0]
    print(two_sum(nums, 0))
    print(three_sum(nums, -10))

