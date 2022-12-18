
def topk(nums, k):

    target = len(nums) - k

    left, right = 0, len(nums)-1

    while left < right:
        partition_index = partition(nums, left, right)

        if partition_index == target:
            return nums[partition_index]
        elif partition_index > target:
            right -= 1
        else:
            left = partition_index + 1


def partition(nums, left, right):
    pivot = nums[left]

    while left < right:

        while left < right and nums[right] >= pivot:
            right -= 1

        nums[left] = pivot

        while left < right and nums[left] <= pivot:
            left += 1

        nums[right] = nums[left]

    nums[left] = pivot
    return left


if __name__ == '__main__':
    nums = [1, 2, 4, 5, 6, 9, 13, 21]
    print(topk(nums, 3))



