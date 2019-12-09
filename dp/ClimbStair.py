# -*-coding:utf-8 -*-


def climb_stair(n):
    """
    爬楼梯的动态规划求法
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [[] for i in range(n)]
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]


if __name__ == "__main__":
    n = 56
    print(climb_stair(n))
