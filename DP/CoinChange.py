
# -*- coding:utf-8 -*-
'''
动态规划
已知不同面值的钞票，求如何用最少数量的钞票组成某个金额，求可以使用的最少钞票数量。如果任意数量的已知面值钞票都无法组成该金额,则返回-1。
'''
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [-1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if (i - coins[j] >= 0) and dp[i - coins[j]] != -1:
                    if (dp[i] == -1 or dp[i] > dp[i - coins[j]] + 1):
                        dp[i] = dp[i - coins[j]] + 1
        '''
        for i in range(len(dp)):
            print("总额为%d 的时候的最少匹配次数为%d" %(i,dp[i]))
        '''
        return dp[amount]

s = Solution()
result = s.coinChange([77,82,84,80,398,286,40,136,162],9794)

print("总额为%d时最少为%d"%(9794,result))