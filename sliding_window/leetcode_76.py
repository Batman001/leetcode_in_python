# -*- coding:utf-8 -*-
from collections import Counter


class Solution:

    def min_window(self, s, t):
        """
        题目简述:
        示例: 给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串
        输入: S = "ADOBECODEBANC", T = "ABC"
        输出: "BANC"
        1. 窗口范围：[l...r]，初始值-[0..-1]。
        2. 辅助变量：target_counter存放t，cur_dict存放当前符合条件的字符。
        3. 移动条件：当前字符串中是否是目标字符串的父集，不是右边界右移动，是左边界右移。
        4. 改变结果：记录符合条件中最短的字符串。
        5. 辅助函数：判断cur_dict中每个key是否在目标集中，每个value是否都小于等于目标集中对应的value。
        :param s:
        :param t:
        :return:
        """
        left, right = 0, -1

        target_counter = Counter(t)
        cur_dict = {}
        found_substr = None

        while left < len(s):

            if right + 1 < len(s) and not self._is_sub(cur_dict, target_counter):
                cur_dict[s[right + 1]] = cur_dict.setdefault(s[right + 1], 0) + 1
                right += 1

            else:
                cur_dict[s[left]] -= 1
                if cur_dict[s[left]] == 0:
                    del cur_dict[s[left]]
                left += 1

            if self._is_sub(cur_dict, target_counter):
                if found_substr is None or right - left + 1 < len(found_substr):
                    found_substr = s[left: right + 1]

        return found_substr if found_substr is not None else ''

    def _is_sub(self, parent, child):
        """
        判断parent 字典中 是否全部包含child 字典 的全部元素
        :param parent:
        :param child:
        :return: True or False
        """
        for k, v in child.items():
            if k not in parent:
                return False
            elif parent[k] < v:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    S = "ADOBECODEBANC"
    t = "ABC"
    print(s.min_window(S, t))