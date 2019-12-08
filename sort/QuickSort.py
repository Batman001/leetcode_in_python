# -*- coding:utf-8 -*-


def quick_sort(array, left, right):
    """
    对数组array进行快速排序
    :param array: 待排序数组
    :param left: 排序数组的左边界开始的排序位置
    :param right: 排序数组的右边界开始的排序位置
    :return:
    """
    if left < right:
        middle_index = get_middle_index(array, left, right)
        quick_sort(array, left, middle_index - 1)
        quick_sort(array, middle_index + 1, right)


def get_middle_index(array, left, right):
    """
    一趟排序 找到中间位置  使得 该位置左边的值都要小于该值 该位置右边的值都要大于该值
    :param array: 数组
    :param left: 左边界
    :param right: 有边界
    :return: 返回middle_index
    """
    # 随机设定的中间值 使之经过一趟排序后 比pivot小的值都在其左边 比pivot大的值都在其右边
    pivot = array[left]

    while left < right:

        while left < right and array[right] > pivot:
            right -= 1
        array[left] = array[right]

        while left < right and array[left] < pivot:
            left += 1
        array[right] = array[left]

    array[left] = pivot
    return left


if __name__ == "__main__":
    arr = [1, 6, 3, 0, -5, -123, 90, 345, 234, 62, 2, 8]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)