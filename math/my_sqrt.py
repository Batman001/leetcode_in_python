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


def my_sqrt_(x):
    """
    二分法求解num的平方根
    :param x: 待开方数
    :return: 开方后的结果
    """
    ans = 0
    if x <= 1:
        return x
    left, right = 1, x
    while left <= right:
        mid = left + ((right - left) >> 1)

        if mid <= x / mid:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans


if __name__ == "__main__":
    print(my_sqrt(256))
    print(my_sqrt_(2568))
