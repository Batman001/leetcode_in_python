# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def remove_k_digits(num: str, k: int) -> str:
        """
        leetcode 402 移掉K位数字
        给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小
        使用贪心算法和递增栈实现
        :param num:
        :param k:
        :return:
        """
        if k >= len(num) == 0:
            return "0"
        stack: List[int] = [int(num[0])]

        for i in range(1, len(num)):
            curr = int(num[i])
            # 注意边界条件stack不为空保证递增栈情形
            while stack != [] and k > 0 and curr < stack[-1]:
                stack.pop()
                k -= 1

            if curr != 0 or stack != []:
                stack.append(curr)

        while k > 0:
            k -= 1
            stack.pop()

        if stack is []:
            return "0"
        stack = [str(item) for item in stack]
        return "".join(stack)


if __name__ == "__main__":
    num = "5337"
    k = 2
    s = Solution()
    res = s.remove_k_digits(num, k)
    print(res)



