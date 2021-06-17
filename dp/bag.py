# -*- coding:utf-8 -*-


def bag(n, cap, weight, value):
    """
    背包问题 在cap允许的范围内 选用价值更多的东西
    :param n: 物品数量 编号从1开始
    :param cap: 背包可以承重的最高质量
    :param weight: 每个物品的质量 按照编号顺序
    :param value:  每个物品的价值 按照编号顺序
    :return: 返回最大价值
    """
    # 设置动态转移矩阵为 n+1 * cap+1
    dp = [[0 for _ in range(cap + 1)] for _ in range(n+1)]

    for i in range(1, n + 1):
        for j in range(1, cap+1):
            # 如果背包的容量的容量小于当前要放入的物品重量
            if j < weight[i]:
                dp[i][j] = dp[i-1][j]
            # 否则需要尝试将当前物品放入背包 保留使得背包内价值最大的选择
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
    print(dp)
    return max(map(max, dp))


if __name__ == "__main__":
    num_things = 4    # 一共有4件物品
    capacity = 8
    weights = {1: 2, 2: 3, 3: 4, 4: 5}
    values = {1: 3, 2: 4, 3: 5, 4: 6}
    print(bag(num_things, capacity, weights, values))
