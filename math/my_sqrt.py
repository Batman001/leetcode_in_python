# -*- coding:utf-8 -*-


def my_sqrt(num):
    """
    leetcode 69 x的平方根
    使用牛顿递归方法 对x进行开放求解
    :param num: 待开方数
    :return: 开方后的结果
    """
    loss = 1e-5
    x = 1.0
    while abs(x * x - num) > loss:
        x = (x + num/x) // 2
    return int(x)


if __name__ == "__main__":
    print(my_sqrt(256))
