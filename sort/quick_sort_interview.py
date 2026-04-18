# -*- coding:utf-8 -*-
# 快速排序 - 百度面试题


def quick_sort(arr, left, right):
    """
    快速排序实现
    :param arr: 待排序数组
    :param left: 左边界
    :param right: 右边界
    """
    if left < right:
        middle_index = get_middle_index(arr, left, right)
        quick_sort(arr, left, middle_index - 1)
        quick_sort(arr, middle_index + 1, right)


def get_middle_index(arr, left, right):
    """
    获取partition位置，使左边小右边大
    :param arr: 数组
    :param left: 左边界
    :param right: 右边界
    :return: partition位置
    """
    pivot = arr[left]

    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]

        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]

    arr[left] = pivot
    return left


def merge_array(left, right):
    """
    合并两个有序数组
    :param left: 左数组
    :param right: 右数组
    :return: 合合后的有序数组
    """
    res = []
    l, l_len, r, r_len = 0, len(left), 0, len(right)

    while l < l_len and r < r_len:
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    if l < l_len:
        res.extend(left[l:])
    else:
        res.extend(right[r:])

    return res


if __name__ == '__main__':
    test_arr = [1, -5, 0, 4, 89, 782, 34, 34, -45]
    print("排序前:", test_arr)
    quick_sort(test_arr, 0, len(test_arr) - 1)
    print("排序后:", test_arr)

    # 合并两个有序数组
    a = [1, 3, 5, 7, 9]
    b = [0, 2, 4, 6, 8, 14, 15]
    print("合并结果:", merge_array(a, b))