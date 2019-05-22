# -*- coding:utf-8 -*-

"""
def quick_sort(num,left,right):
    if left>=right:                    #如果只有一个数字时，结束递归
        return
    flag=left          #是L 不是1
    for i in range(left+1,right+1):    #以第一个数字作为基准，从第二个数开始比较
        if num[flag]>num[i]:
            tmp=num[i]
            del num[i]
            num.insert(flag,tmp)
            flag+=1
    quick_sort(num,left,flag-1)     #将基准的 前后部分分别递归排序
    quick_sort(num,flag+1,right)

num=[1,-9,5,7,9,3,2,8]
quick_sort(num,0,7)
print(num)
"""


def quick_sort(array, left, right):
    if left >= right:
        return array
    low = left
    high = right
    key = array[left]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    print(array[:left])
    print(array[left:])

    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)
    # print(left == right)
    return array


if __name__ == "__main__":
    array = [2, 7, 3]
    quick_sort(array, 0, len(array) - 1)
    print(array)


