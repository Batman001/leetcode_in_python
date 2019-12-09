# -*- coding:utf-8 -*-


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    查找两个字符串的最长公共序列
    :param text1: 字符串1
    :param text2: 字符串2
    :return: 最长公共序列的长度
    """
    m = len(text1)
    n = len(text2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


if __name__ == "__main__":
    str1 = "abcde"
    str2 = "ace"
    print(longest_common_subsequence(str1, str2))