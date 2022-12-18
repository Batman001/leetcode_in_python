
def findKthNum(nums, k):
    """
    获取nums数组中第k大的元素
    :param nums:
    :param k:
    :return:
    """
    target = len(nums) - k

    left, right = 0, len(nums)-1

    while True:
        partition_index = get_index(nums, left, right)

        if partition_index == target:
            return nums[partition_index]
        elif partition_index > target:
            right = partition_index - 1
        else:
            left = partition_index + 1


def get_index(nums, left, right):
    """
    快排思想 返回partition_index, 使得左边小 右边大
    :param nums:
    :param left:
    :param right:
    :return:
    """

    pivot = nums[left]

    while left < right:

        while left < right and nums[right] >= pivot:
            right -= 1

        nums[left] = nums[right]

        while left < right and nums[left] <= pivot:
            left += 1

        nums[right] = nums[left]

    nums[left] = pivot

    return left


if __name__ == '__main__':
    nums = [34, 22, 9, 5, 68, 71, 78, 23]
    target = findKthNum(nums, 6)
    print(target)

