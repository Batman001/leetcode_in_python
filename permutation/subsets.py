# -*- coding:utf-8 -*-

def subsets(nums):
    res = []
    temp = []
    dfs(res, temp, nums, 0)
    return res


def dfs(res, temp, nums, index):
    res.append(temp[:])
    for i in range(index, len(nums)):
        temp.append(nums[i])
        dfs(res, temp, nums, i+1)
        temp.pop(-1)


if __name__ == "__main__":
    result = subsets([1, 2, 3, 4])
    print(result)
    print(len(result))



