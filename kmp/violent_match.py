# -*- coding:utf-8 -*-


def violent_match(main_str, mode_str):
    """
    暴力匹配模式串与主串
    :param main_str: 主字符串
    :param mode_str: 模式字符串
    :return: 匹配成功的主字符串的索引，否则返回-1
    """
    # 主串开始的位置
    i = 0
    # 模式字符串开始的位置
    j = 0

    while i < len(main_str) and j < len(mode_str):
        if main_str[i] == mode_str[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    # 如果模式字符串匹配完成 即是模式字符串匹配到最后
    # 由于最后一个字符也需要匹配 因此最后会有 i+=1 j+=1
    if j == len(mode_str):
        return i - j
    else:
        return -1


if __name__ == "__main__":
    print(violent_match("Hello world", "or"))
