# -*- coding:utf-8 -*-
from collections import Counter


class Solution:

    @staticmethod
    def find_anagrams(self, s, p):
        """
        给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
        :param s: 字符串s
        :param p: 非空字符串p
        :return: 返回满足条件子串的起始索引
        """
        # 左右索引
        left, right = 0, -1
        # target_counter存放p，cur_dict存放当前符合条件的字符。
        target_counter, target_len = Counter(p), len(p)
        cur_dict = {}

        found_indexes = []

        while left < len(s):

            # 如果窗口长度小于target_len 则右边界移动
            if right + 1 < len(s) and right - left + 1 < target_len:
                # dict.setdefault方法是 操作字典 如键不已经存在于字典中，将会添加键并将值设为默认值
                cur_dict[s[right + 1]] = cur_dict.setdefault(s[right + 1], 0) + 1
                right += 1

            # 否则左边界移动
            else:
                cur_dict[s[left]] -= 1
                if cur_dict[s[left]] == 0:
                    cur_dict.pop(s[left])

                left += 1

            # target_counter与cur_dict一样，则记录当前left。
            if right - left + 1 == target_len and target_counter == cur_dict:
                found_indexes.append(left)

        return found_indexes





