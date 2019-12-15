

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


def permute(string):
    """
    对str进行全排列算法
    :param string:
    :return: 全排列算法的结果 用列表存储
    """
    len_str = len(string)
    # 递归出口
    if len_str < 2:
        return string

    res = []
    for i in range(len_str):
        cur_str = string[i]
        rest_str = string[:i] + string[i+1:]

        for item in permute(rest_str):
            res.append(item + cur_str)
    return res


if __name__ == "__main__":
    main1()
    print(permute("ABC"))
