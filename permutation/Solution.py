# -*- coding:utf-8 -*-
class Solution(object):

    def permute(self, nums):
        print("nums", nums)
        if len(nums) <= 1:
            return [nums]
        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            print(nums[:i], "+", nums[i+1:], "=", n)
            for y in self.permute(n):
                print("递归内：")
                print([num], "+", y, "=", [num] + y)
                ans.append([num] + y)
            print("------end-------")

        return ans

    def permute_(self, nums):
        self.res = []
        sub = []
        self.dfs(nums, sub)
        return self.res

    def dfs(self, nums, sub_list):
        if len(sub_list) == len(nums):
            self.res.append(sub_list[:])

        for m in nums:
            if m in sub_list:
                continue
            sub_list.append(m)
            self.dfs(nums, sub_list)
            sub_list.remove(m)


if __name__ == "__main__":
    nums = [1, 2, 3]
    s = Solution()
    result = s.permute_(nums)
    print(result)
