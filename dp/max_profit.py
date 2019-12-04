# -*- coding:utf-8 -*-
class Solution:

    @staticmethod
    def max_profit(prices):
        """
        leetcode121 买卖股票的最佳时机
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
        如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
        链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
        :solution 使用动态规划算法求解
        :param prices: 最近几天的股票的价格 int数组
        :return: 返回最大利润
        """
        if len(prices) <= 1:
            return 0
        buy_min = prices[0]
        max_profit = 0
        # 第i天的最大利润 = max(前i-1天的最大利润, 第i天的价格-前i-1天中的最小price)
        for i in range(len(prices)):
            buy_min = min(buy_min, prices[i])
            max_profit = max(max_profit, prices[i] - buy_min)
        return max_profit

    @staticmethod
    def max_profit_(prices):
        """
        leetcode122 买卖股票的最佳时机
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
        你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        :solution 使用动态规划加贪心算法求解(如果今天价格比昨天高，就直接卖出）
        :param prices: 最近几天的股票的价格 int数组
        :return: 返回最大利润
        """
        if len(prices) <= 1:
            return 0
        max_profit = 0
        buy_in = prices[0]
        for i in range(len(prices)):
            if prices[i] < buy_in:
                buy_in = prices[i]
            else:
                cur_profit = prices[i] - buy_in
                max_profit += cur_profit
                buy_in = prices[i]
        return max_profit

    @staticmethod
    def max_profit_2(prices):
        """
        leetcode 122
        :param prices: 股票价格的数组
        :return: 交易能获得的最大收益
        贪心算法（只要今天比昨天价格高，就要进行交易）
        """
        if len(prices) <= 1:
            return 0
        return sum(max(prices[i] - prices[i-1], 0) for i in range(1, len(prices)))

    @staticmethod
    def max_profit_3(self, prices):
        """
        leetcode 123买卖股票的最佳时机 III
        给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
        :param prices: 股票价格的数组 三维动态规划
        :return:交易能获得的最大收益
        """
        # 第一种方法：标准的三维DP动态规划，三个维度，第一维表示天，第二维表示交易了几次，
        # 第三维表示是否持有股票。与下面188题买卖股票4一样的代码，
        # 把交易k次定义为2次。当然也可以把内层的for循环拆出来，分别列出交易0次、1次、2次的状态转移方程即可
        if not prices:
            return 0
        n = len(prices)
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]
        # dp[i][j][0]表示第i天交易了j次时不持有股票, dp[i][j][1]表示第i天交易了j次时持有股票
        # 定义卖出股票时交易次数加1
        for i in range(3):
            dp[0][i][0], dp[0][i][1] = 0, -prices[0]

        for i in range(1, n):
            for j in range(3):
                if not j:
                    dp[i][j][0] = dp[i - 1][j][0]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])

        return max(dp[n - 1][0][0], dp[n - 1][1][0], dp[n - 1][2][0])

    @staticmethod
    def max_profit_4(prices):
        """
        leetcode 123买卖股票的最佳时机 III
        :param prices:
        :return:
        """
        buy1, buy2 = float('-inf'), float('-inf')
        sell1, sell2 = 0, 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, price + buy1)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, price + buy2)
        return sell2


if __name__ == "__main__":
    s = Solution()
    test_prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(s.max_profit_4(test_prices))




