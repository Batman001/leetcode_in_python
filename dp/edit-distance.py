# -*- coding:utf-8 -*-


def edit_distance(word1, word2):
    """
    leetcode 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数
    https://leetcode-cn.com/problems/edit-distance/
    使用动态规划求解两个单词的编辑距离
    :param word1: word1
    :param word2: word2
    :return: 返回最少操作次数
    """
    m = len(word1)
    n = len(word2)

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # 处理第一行的编辑距离
    for i in range(n+1):
        dp[0][i] = i

    # 处理第一列的编辑距离
    for j in range(m+1):
        dp[j][0] = j

    # 动态更新剩余的操作次数矩阵
    for i in range(1, m+1):
        for j in range(1, n+1):
            # 如果word1的前i个字符的最后一个字符word1[i-1] 与
            # word2的前j个字符的最后一个字符 word2[j-1]一致的话
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    return dp[m][n]

