# -*- coding:utf-8 -*-
'''
from collections import Counter

def minWindow(s, t):
    if (len(s) == 0 or len(t) == 0):
        return ""

    result = ""
    match_count = 0
    t_count = dict(Counter(t))
    s_count = dict(zip(" ".join(t).split(), [0] * len(t)))

    left = find_index(0, s, t_count)
    if (left == len(s)):
        return ""
    right = left
    while (right < len(s)):
        if t_count[s[right]] > s_count[s[right]]:
            match_count += 1
        s_count[s[right]] += 1          #l
        while (left < len(s) and match_count == len(t)):
            if len(result) == 0 or len(result) > right - left + 1:
                result = s[left:right + 1]
            if s_count[s[left]] <= t_count[s[left]]:
                match_count -= 1

            s_count[s[left]] -= 1
            left = find_index(left + 1, s, t_count)
        right = find_index(right + 1, s, t_count)
    return result


def find_index(start, s, t_count):
    while (start < len(s)):
        if s[start] in t_count:
            return start
        start += 1
    return start

'''

from collections import Counter



class Solution(object):
    '''
    LeetCode 76 hard Minimum Window SubString
    '''
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0 or len(t) == 0:
            return ""
        result = ""

        t_count = Counter(t)
        s_count = dict(zip(" ".join(t).split(), [0] * len(t)))
        left = self.find_index(0, s, t_count)
        right = left
        count_match = 0
        if left == len(s):
            return ""
        while (right < len(s)):
            if t_count[s[right]] > s_count[s[right]]:
                count_match += 1
            s_count[s[right]] += 1
            while (left < len(s) and count_match == len(t)):
                if (len(result) == 0 or len(result) > right - left + 1):
                    result = s[left:right + 1]
                if (s_count[s[left]] <= t_count[s[left]]):
                    count_match -= 1
                s_count[s[left]] -= 1
                left = self.find_index(left + 1, s, t_count)
            right = self.find_index(right + 1, s, t_count)
        return result

    def find_index(self, start, s, t_count):
        while (start < len(s)):
            if s[start] in t_count:
                return start
            start += 1
        return start

s = "ADOBACODEBANC"
t = "ABC"
solution = Solution()
print(solution.minWindow(s,t))