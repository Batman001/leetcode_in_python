# -*- coding:utf-8 -*-
# LeetCode 78: 子集


def subsets(nums):
    """
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）
    :param nums: 整数数组
    :return: 所有子集列表
    """
    res = []
    temp = []
    dfs(res, temp, nums, 0)
    return res


def dfs(res, temp, nums, index):
    """
    DFS递归生成子集
    :param res: 结果列表
    :param temp: 当前子集
    :param nums: 原数组
    :param index: 当前索引
    """
    res.append(temp[:])
    for i in range(index, len(nums)):
        temp.append(nums[i])
        dfs(res, temp, nums, i + 1)
        temp.pop(-1)


if __name__ == "__main__":
    result = subsets([1, 2, 3])
    print("子集结果:", result)
    print("子集数量:", len(result))