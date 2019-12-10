# -*- coding:utf-8 -*-


class Solution:

    @staticmethod
    def coin_change(coins, amount):
        """
        动态规划
        已知不同面值的钞票，求如何用最少数量的钞票组成某个金额，求可以使用的最少钞票数量。如果任意数量的已知面值钞票都无法组成该金额,则返回-1。
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if (i - coins[j] >= 0) and dp[i - coins[j]] != -1:
                    if dp[i] == -1 or dp[i] > dp[i - coins[j]] + 1:
                        dp[i] = dp[i - coins[j]] + 1
        '''
        for i in range(len(dp)):
            print("总额为%d 的时候的最少匹配次数为%d" %(i,dp[i]))
        '''
        return dp[amount]

    @staticmethod
    def coin_change_(coins, amount):
        """
        动态规划 比如说demo例子  递归逻辑为： f(11) = min(f(10), f(9), f(6)) + 1
        :param coins: [1,2,5] 可以选择的硬币面值
        :param amount: [11]   要换的钱的总数
        :return: 可以使用的最少硬币数量
        """
        if amount < 0:
            return -1
        dp = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            # 设置每一个dp[i]的默认cost为正无穷
            cost = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    cost = min(cost, dp[i-coin] + 1)
            dp[i] = cost

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100]
    amount = 189
    s = Solution()

    print("总额为%d时最少为%d" % (amount, s.coin_change_(coins, amount)))
    print(s.coin_change_(coins, amount))
