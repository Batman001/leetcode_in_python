# -*- coding:utf-8 -*-
# leetcode215. 数组中的第K个最大元素 https://leetcode.cn/problems/kth-largest-element-in-an-array/

def build_heap(array):

    for i in range(len(array)//2-1, -1, -1):
        minify(array, i)
    return array


def minify(array, i):
    left, right = i * 2 + 1, i * 2 + 2
    length, min_index = len(array), i

    if left < length and array[left] < array[min_index]:
        min_index = left

    if right < length and array[right] < array[min_index]:
        min_index = right

    if min_index != i:
        array[i], array[min_index] = array[min_index], array[i]
        minify(array, min_index)


def heap_sort(heap):
    result = []
    for i in range(len(heap)):
        heap_size = len(heap)
        heap[0], heap[heap_size - 1] = heap[heap_size-1], heap[0]
        # 此时最小值已经交换至堆尾
        result.append(heap.pop(-1))
        minify(heap, 0)
    return result


def get_top_k(array, k):
    select_array = array[:k]
    heap = build_heap(select_array)
    for i in range(k, len(array)):
        if array[i] > heap[0]:
            heap[0] = array[i]
            minify(heap, 0)
    sorted_heap = heap_sort(heap)
    print("前k大的数组为:", sorted_heap)
    print("第k大的元素为:", sorted_heap[0])
    return sorted_heap[0]


def find_k_largest_num(nums, k):
    """
    使用快排的思想找到数组中第k大元素
    :param nums: 数组
    :param k: 第k大
    :return: 数值
    """
    target = len(nums) - k
    left, right = 0, len(nums)-1

    while True:
        partition_index = partitions(nums, left, right)
        if partition_index == target:
            return nums[partition_index]
        elif partition_index > target:
            right -= partition_index - 1
        else:
            left = partition_index + 1


def partitions(nums, left, right):
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


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 25, 564, 683, 26, 675]
    array_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 25, 564, 683, 26, 675]
    get_top_k(array, 9)

    print('快排思想中，第9大的元素为: ', find_k_largest_num(array_, 9))

