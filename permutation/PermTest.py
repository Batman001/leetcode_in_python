
'''
result = []
def perm(list,stack):
    if not list:
        print (stack)
        result.append(stack)
    else:
        for i in range(len(list)):
            stack.append(list[i])
            del list[i]
            perm(list,stack)
            list.insert(i,stack.pop())


if __name__ == '__main__':
    list = [1,2,3]
    stack = []
    perm(list, stack)
    print(result)
'''
'''

import copy

all = [1, 2, 3, 4]
result = []


def fun_fron(remain_list, res_list):
    if len(remain_list) == 1:
        res_list.append(remain_list[0])
        print (res_list)
        result.append(res_list)
    else:
        for j in range(len(remain_list)):
            remain_list_c = copy.deepcopy(remain_list)
            res_list_c = copy.deepcopy(res_list)
            twp = remain_list_c.pop(j)
            res_list_c.append(twp)
            fun_fron(remain_list_c, res_list_c)


fun_fron(all, [])

print (len(result))

'''


def perm(array, begin, end):
    if begin == end:
        print(array)
    for i in range(begin, end + 1):
        swap(array, i, begin)
        perm(array, begin+1, end)
        swap(array, i, begin)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def main1():
    array = [1, 2, 3, 5, 6, 7]
    perm(array, 0, len(array)-1)


def merge(left, right):
    l_len = len(left)
    r_len = len(right)
    i, j = 0, 0
    result = []
    while i < l_len and j < r_len:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(nums):
    if len(nums)==1:
        return nums
    mid = len(nums)/2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def main2():
    array = [1, 5, 3, 9, 6, 7, 19, 26]
    sort_array = merge_sort(array)
    print(sort_array)


if __name__ == "__main__":
    main1()
    main2()