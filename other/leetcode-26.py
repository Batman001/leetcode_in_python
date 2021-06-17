
# leetcode -26
def remove_duplicates(nums):
    if not nums:
        return 0
    index = 0

    for i in range(index+1, len(nums)):
        if nums[i] == nums[index]:
            continue
        else:
            index += 1
            nums[index] = nums[i]

    return index + 1


# nums = [1, 1, 2]
# nums_len = remove_duplicates(nums)


# leetcode -33
def search(nums, target):
    # 首先寻找旋转数组的位置
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    rotate_index = l

    ans = binary_search(nums[:rotate_index], target)
    if ans == -1:
        ans = binary_search(nums[rotate_index:], target)

        if ans != -1:
            ans += rotate_index
    return ans


def binary_search(nums, target):
    index = -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            index = mid
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return index


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))