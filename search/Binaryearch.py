# -*- coding:utf-8 -*-


def search_array(sort_array, target, begin, end):
    """二分查找递归实现 """
    if begin > end:
        return False
    mid = (begin+end) // 2
    if target == sort_array[mid]:
        return True
    elif target < sort_array[mid]:
        return search_array(sort_array, target, begin, mid - 1)
    else:
        return search_array(sort_array, target, mid+1, end)


def search_array_(sort_array, target):
    """二分查找递归实现 """
    begin = 0
    end = len(sort_array) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if target == sort_array[mid]:
            return True
        elif target > sort_array[mid]:
            begin = mid + 1
        else:
            end = mid - 1
    return False


def search_insert(sort_nums, target):
    """
    给定一个排序数组nums(无重复元素)与目标值target，
    如果target在nums里出现，则返回target所在下标，
    如果target在nums里未出现，则返回target应该插入位置的数组下标，
    使得将target插入数组nums后，数组仍有序
    """
    begin = 0
    end = len(sort_nums) - 1
    index = -1
    while index == -1:
        mid = (begin+end) // 2
        if target == sort_nums[mid]:
            index = mid
        elif target > sort_nums[mid]:
            if mid == len(sort_nums)-1 or target < sort_nums[mid + 1]:
                index = mid + 1
            begin = mid + 1
        else:
            if target > sort_nums[mid - 1] or mid == 0:
                index = mid
            end = mid - 1
    return index


def search_range(nums, target):
    """
    给定一个排序数组nums(nums中有重复元素)与目标值target，
    如果target在nums里出现，则返回target所在区间的左右端点下标，[左端点, 右端点]，
    如果target在nums里未出现，则返回[-1, -1]
    """

    def left_bound(nums_, target_):
        begin = 0
        end = len(nums_) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if target_ == nums_[mid]:
                if mid == 0 or nums_[mid - 1] < target_:
                    return mid
                end = mid - 1
            elif target_ > nums_[mid]:
                begin = mid + 1
            else:
                end = mid - 1
        return -1

    def right_bound(nums_, target_):
        begin = 0
        end = len(nums_) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if target_ == nums_[mid]:
                if mid == len(nums_)-1 or target_ < nums_[mid + 1]:
                    return mid
                begin = mid + 1
            elif target_ > nums_[mid]:
                begin = mid + 1
            else:
                end = mid - 1

    left_index = left_bound(nums, target)
    right_index = right_bound(nums, target)
    return [left_index, right_index]


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

    left = 0
    right = len(matrix)
    row_loc = 0
    while left < right:
        mid = (left + right) // 2
        if matrix[mid][0] == target:
            return True
        if matrix[mid][0] < target:
            row_loc = mid
            left = mid + 1
        else:
            right = mid

    print("该数应该出现在第几列？", row_loc)

    l, r = 0, len(matrix[0])

    while l < r:
        mid = (l + r) // 2
        if matrix[row_loc][mid] == target:
            return True
        if matrix[row_loc][mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False


if __name__ == "__main__":

    # a = [-1, 2, 5, 20, 90, 100, 207, 800]
    # b = [50, 90, 3, -1, 207, 80]
    #
    # result = []
    # result_ = []
    #
    # for item in b:
    #     result.append(search_array(a, item, 0, len(a)))
    #     result_.append(search_array_(a, item))
    # # print(u"递归实现二分查找结果如下", result)
    # # print(u"非递归实现二分查找", result_)
    #
    # print(search_insert(a, 890))
    #
    # sort_dup_list_1 = [1, 2, 4, 4, 4, 4, 5, 89, 90]
    # sort_dup_list_2 = [2, 2, 2, 2, 4]
    # sort_dup_list_3 = [1, 2, 3, 3, 3, 3, 3]
    # print(search_range(sort_dup_list_3, 3))

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    print(search_matrix(matrix, target))
