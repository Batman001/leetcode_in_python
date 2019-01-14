# -*- coding:utf-8 -*-
import numpy as np

def get_next_array(modestr):
    """
    计算得到模式字符串的next数组
    :param modestr:
    :return:
    """
    NextArray = np.zeros(shape = (len(modestr),), dtype='int32')
    NextArray[0] = -1
    i = 0
    j = -1

    # while not finish whole modestr
    while i < len(modestr) - 1:
        if j == -1 or modestr[i] == modestr[j]:
            # if first element of substring or match, check next
            i += 1
            j += 1
            NextArray[i] = j
        else:
            # not match, jump to next j
            j = NextArray[j]
    return NextArray


def KMP_Algorithm(mainStr, modeStr):
    """
    KMP字符串匹配算法实现
    :param mainStr:  主字符串
    :param modeStr:  模式字符串
    :return: 匹配成功的主字符串的索引，否则返回-1
    """
    NextArray = get_next_array(modeStr)
    i, j = 0, 0
    # while not finish loop
    while i < len(mainStr) and j < len(modeStr):
        # if first of modeStr or match, check next
        if j == -1 or mainStr[i] == modeStr[j]:
            i += 1
            j += 1
        else:
            j = NextArray[j]
    if j == len(modeStr):
        return i - j
    else:
        return -1

if __name__ == "__main__":

    print(KMP_Algorithm("hello World", "or"))
