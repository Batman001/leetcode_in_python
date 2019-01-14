# -*- coding:utf-8 -*-


'''
二分查找递归实现
'''
def searchArray(sortArray, target, begin, end):
    if(begin>end):
        return False
    mid = (begin+end)/2
    if (target == sortArray[mid]):
        return True
    elif target < sortArray[mid]:
        return searchArray(sortArray, target, begin, mid - 1)
    else:
        return searchArray(sortArray, target, mid+1, end)

def searchArray_(sortArray, target):
    begin = 0
    end = len(sortArray) - 1
    while(begin <= end):
        mid = (begin + end)/2
        if target == sortArray[mid]:
            return True
        elif target > sortArray[mid]:
            begin  = mid +1
        else:
            end = mid -1
    return False



'''
给定一个排序数组nums(无重复元素)与目标值target，
如果target在nums里出现，则返回target所在下标，
如果target在nums里未出现，则返回target应该插入位置的数组下标，
使得将target插入数组nums后，数组仍有序
'''
def searchInsert(sortnums, target):
    begin = 0
    end = len(sortnums)-1
    index = -1
    while(index == -1):
        mid = (begin+end)/2
        if target == sortnums[mid]:
            index = mid
        elif target > sortnums[mid]:
            if mid == len(sortnums)-1 or target < sortnums[mid + 1]:
                index = mid +1
            begin = mid + 1
        else:
            if target > sortnums[mid-1] or mid == 0:
                index = mid
            end = mid - 1
    return index

'''
给定一个排序数组nums(nums中有重复元素)与目标值target，
如果target在nums里出现，则返回target所在区间的左右端点下标，[左端点, 右端点]，
如果target在nums里未出现，则返回[-1, -1]
'''
def searchRange(nums, target):

    def left_bound(nums, target):
        begin = 0
        end = len(nums)-1
        while(begin<=end):
            mid = int((begin+end)/2)
            if target == nums[mid]:
                if mid == 0 or nums[mid-1]<target:
                    return mid
                end = mid - 1
            elif target > nums[mid]:
                begin = mid + 1
            else:
                end = mid - 1
        return -1

    def right_bound(nums, target):
        begin = 0
        end = len(nums) - 1
        while(begin<=end):
            mid = int((begin+end)/2)
            if target == nums[mid]:
                if mid == len(nums)-1 or target<nums[mid+1]:
                    return mid
                begin = mid + 1
            elif target > nums[mid]:
                begin = mid + 1
            else:
                end = mid - 1

    left_index = left_bound(nums, target)
    right_index = right_bound(nums, target)
    return [left_index, right_index]


if __name__ == "__main__":

    a = [-1, 2, 5, 20, 90, 100, 207, 800]
    b = [50, 90, 3, -1, 207, 80]

    result = []
    result_ = []

    for item in b:
        result.append(searchArray(a,item,0,len(a)))
        result_.append(searchArray_(a, item))
    #print(u"递归实现二分查找结果如下", result)
    #print(u"非递归实现二分查找", result_)

    print(searchInsert(a, 890))


    sort_dup_list_1 = [1,2,4,4,4,4,5,89,90]
    sort_dup_list_2 = [2,2,2,2,4]
    sort_dup_list_3 = [1,2,3,3,3,3,3]
    print(searchRange(sort_dup_list_3, 3))