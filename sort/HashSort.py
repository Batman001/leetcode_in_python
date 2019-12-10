# -*- coding:utf-8 -*-


def hash_sort(array, max_value):
    """
    需要设定当前hash排序的最大不重复数字 最大值为max_value
    哈希排序数字必须为非负数才行
    同时要保证哈希表的长度要超过最大数字
    :param array: 待排序数组
    :param max_value 当前数组的最大值
    :return: 排序好的数组
    """
    hash_array = [0 for _ in range(max_value+1)]

    # 遍历整个array数组
    for i in range(len(array)):
        hash_array[array[i]] += 1

    sorted_array = []
    for i in range(len(hash_array)):
        if hash_array[i] == 1:
            sorted_array.append(i)
    return sorted_array


if __name__ == "__main__":
    nums = [999, 1, 44, 6, 234, 78, 1, 54, 8, 44, 89, 45, 345,
             235, 56, 234, 567, 23, 57, 23, 57, 13, 57, 12, 45, 74, 12, 90, 1000]
    print(hash_sort(nums, 1000))


