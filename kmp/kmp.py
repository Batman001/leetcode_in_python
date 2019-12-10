# -*- coding:utf-8 -*-
import numpy as np


def get_next_array(mode_str):
    """
    计算得到模式字符串的next数组
    :param mode_str:模式串
    :return: 模式字符串的next数组
    """
    next_array = np.zeros(shape=(len(mode_str),), dtype='int32')
    next_array[0] = -1
    i = 0
    j = -1

    # while not finish whole mode_str
    while i < len(mode_str) - 1:
        if j == -1 or mode_str[i] == mode_str[j]:
            # if first element of substring or match, check next
            i += 1
            j += 1
            next_array[i] = j
        else:
            # not match, jump to next j
            j = next_array[j]
    return next_array


def kmp_algorithm(main_str, mode_str):
    """
    KMP字符串匹配算法实现
    :param main_str:  主字符串
    :param mode_str:  模式字符串
    :return: 匹配成功的主字符串的索引，否则返回-1
    """
    next_array = get_next_array(mode_str)
    i, j = 0, 0
    # while not finish loop
    while i < len(main_str) and j < len(mode_str):
        # if first of modeStr or match, check next
        if j == -1 or main_str[i] == mode_str[j]:
            i += 1
            j += 1
        else:
            j = next_array[j]
    if j == len(mode_str):
        return i - j
    else:
        return -1


if __name__ == "__main__":

    # print(kmp_algorithm("hello World", "or"))

    print(kmp_algorithm("abbaabbaaba", "abbaaba"))
