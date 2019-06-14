# -*- coding:utf-8 -*-

"""
哈希排序数字必须为非负数才行
同时要保证哈希表的长度要超过最大数字
"""
array = [999, 1, 44, 6, 234, 78, 1, 54, 8, 44, 89, 45, 345,
         235, 56, 234, 567, 23, 57, 23, 57, 13, 57, 12, 45, 74, 12, 90]


hash_array = [0 for i in range(1000)]

for i in range(len(array)):
    hash_array[array[i]] += 1

for i in range(1000):
    for j in range(hash_array[i]):
        print(i)
