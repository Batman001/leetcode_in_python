# -*- coding:utf-8 -*-


class Solution:

    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        leetcode 125
        示例：
        输入: "A man, a plan, a canal: Panama"
        输出: true
        使用双指针验证回文字符串
        :param s: 待验证字符串
        :return: 返回boolean 是否为回文字符串
        """
        s = ''.join(filter(str.isalnum, s)).lower()
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    test_str = "A man, a plan, a canal: Panama"
    print(solution.is_palindrome(test_str))
