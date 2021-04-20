# -*- coding:utf-8 -*-

def search_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    二分查找实现
    step1: 先在第一列上二分查找，寻找目标值所在列
    step2: 在目标列执行二分查找，判断target是否存在
    """
    if matrix is None or matrix == [[]]:
        return False
    col = len(matrix)

    left = 0
    right = col
    while left < right:
        mid = (left + right) // 2
        if matrix[mid][0] == target:
            return True
        if matrix[mid][0] < target:
            left = mid + 1
        else:
            right = mid
    # target row，即target所在行 使用tmp表示
    tmp = mid
    l, r = 0, len(matrix[0]) - 1

    while l < r:
        mid = (l + r) // 2
        if matrix[tmp][mid] == target:
            return True
        if matrix[tmp][mid] < target:
            l = mid + 1
        else:
            r = mid
    return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50], [60, 61, 72, 83], [85, 86, 90, 92], [93, 95, 96, 98]]
    target = -9
    print(search_matrix(matrix, target))
