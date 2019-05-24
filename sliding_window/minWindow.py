# -*- coding:utf-8 -*-
from collections import Counter


class Solution:

    def min_window(self, s, t):
        """
        :param s: str 全部字符串
        :param t: str 部分字符串
        给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串
        （1）left,right指针同时向前移动 直到找到部分字符串中包含的字符
        （2）然后left指针固定
        （3）right指针向前移动 直到 s[left:right+1] 窗口中包含t字符串 将其存入满足条件子串列表中
        （4）随后left指针向前移动 找到下一个部分字符串中包含的字符位置

        left == len(s)-len(t)

        :return:
        """
        if len(s) == 0 or len(t) == 0:
            return ""
        if len(s) < len(t):
            return ""
        if s == t:
            return t
        length = len(s)
        all_match_indexes = []
        res = s
        for i in range(length):
            if s[i] in t:
                all_match_indexes.append(i)

        match_substr = []
        if len(all_match_indexes) == 1:
            return t
        for i in range(len(all_match_indexes)):
            left = all_match_indexes[i]
            for j in range(i+1, len(all_match_indexes)):
                right = all_match_indexes[j]
                if self.match(s, t, left, right):
                    match_substr.append(s[left:right+1])
                    break
                else:
                    pass

        if match_substr == []:
            return ""
        else:
            for item in match_substr:
                if len(item) <= length:
                    res = item
        return res

    def match(self, s, t, left, right):
        """
        判断s[left:right+1] 是否包含子串t
        :param self:
        :param s: 字符串
        :param t: 子串
        :param left: 左边索引
        :param right: 右边索引
        :return: true or false
        """
        current_str = s[left:right + 1]
        match_str = list(t)
        for char in current_str:
            if char in match_str:
                match_str.remove(char)
        if match_str == []:
            return True
        else:
            return False


if __name__ == "__main__":
    S = "ADOBECODEBANC"
    T = "ABC"
    s1 = "ab"
    t = "a"
    s = Solution()
    result = s.min_window(s1, t)
    print(result)












