# -*- coding:utf-8 -*-


def merge(left, right):
    """
    合并left和right 并用result进行存储
    :param left: 待合并的左边数组列表
    :param right: 待合并的右边数组列表
    :return: 返回合并后的结果
    """
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    """
    归并排序的主程序
    :param lists: 待归并排序的列表
    :return:
    """

    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left_array = merge_sort(lists[:num])
    right_array = merge_sort(lists[num:])
    return merge(left_array, right_array)


if __name__ == "__main__":
    a = [5, 1, 2, 4, 3, 8, 9, 3, 4, 7, 10, 8]
    print(merge_sort(a))
