# -*- coding:utf-8 -*-
# 买卖股票的最佳时机 - LeetCode 121
# 百度面试题


def get_max_value(nums):
    """
    动态规划方法求解最大利润
    :param nums: 价格数组
    :return: 最大利润
    """
    dp = [0 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] - min(nums[0:i]))
    return dp[-1]


def get_max_profit(nums):
    """
    一次遍历方法求解最大利润 (更优解)
    :param nums: 价格数组
    :return: 最大利润
    """
    cost, profit = float("inf"), 0
    for num in nums:
        cost = min(cost, num)
        profit = max(profit, num - cost)
    return profit


if __name__ == '__main__':
    prices = [3, 4, 9, 5, 20, 2, 6]
    print("股票价格:", prices)
    print("最大利润(DP方法):", get_max_value(prices))
    print("最大利润(一次遍历):", get_max_profit(prices))