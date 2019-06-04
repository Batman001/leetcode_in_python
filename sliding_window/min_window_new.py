# -*- coding:utf-8 -*-
import collections


class Solution:

    @staticmethod
    def min_window(self, s, t):

        count = collections.Counter(t)  # 统计字符串 t 中字符出现的次数
        miss = len(t)  # miss 负责记录 当前窗口是否满足条件
        i = m = n = 0
        for j, v in enumerate(s, start=1):  # 向右滑动或扩展
            miss -= (count[v] > 0)
            count[v] -= 1
            if not miss:  # 当前窗口满足条件
                while i < j and count[s[i]] < 0:  # 左边界收缩
                    count[s[i]] += 1
                    i += 1
                if not n or j-i <= n-m:  # 更新新的窗口
                    n, m = j, i
        return s[m:n]


if __name__ == '__main__':
    solution = Solution()
    s, t = 'ADOBECODEBANC', 'ABC'
    print(solution.min_window(s, t))