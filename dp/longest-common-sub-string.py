# -*- coding:utf-8 -*-


def longest_common_sub_string(text1: str, text2: str) -> int:
    """
    寻找两个字符串的最长公共子串
    :param text1: 字符串1
    :param text2: 字符串2
    :return: 最长公共子串的长度
    """
    m = len(text1)
    n = len(text2)

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0

    return max(map(max, dp))


if __name__ == "__main__":
    str1 = "asdfas"
    str2 = "werasdfswer"
    print(longest_common_sub_string(str1, str2))
