# -*- coding:utf-8 -*-


def solution(s):
    result = 0
    i = 0
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    while i < len(s) - 1:
        if (s[i] + s[i + 1]) in romans:
            result += numbers[romans.index(s[i] + s[i + 1])]
            print("加 2 " + str(i))
            i += 2
            print("加 2 后" + str(i))

        else:
            result += numbers[romans.index(s[i])]
            print("加 1 " + str(i))
            i += 1
            print("加 1 后" + str(i))
    print(i)
    if i == len(s) - 1:
        result += numbers[romans.index(s[i])]
    return result

