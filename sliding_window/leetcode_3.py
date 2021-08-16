# -*- coding:utf-8 -*-


class Solution:

    @staticmethod
    def length_longest_substring(self, s):
        """
        leetcode 3 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度
        :param s:
        :return:
        """
        max_len = 0
        left, right = 0, -1
        # 终止条件
        while left < len(s):
            # 终止条件
            if right + 1 < len(s) and s[right+1] not in s[left:right+1]:
                right += 1
            else:
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len


def solution_test(s):
    left, right = 0, 1
    max_len = 0
    while left < len(s):
        if right+1 < len(s) and s[right+1] not in s[left: right+1]:
            right += 1
        else:
            left += 1
        max_len = max(max_len, right-left+1)
    return max_len


if __name__ == '__main__':
    print(solution_test("abcabcbb"))



