# -*- coding:utf-8 -*-

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def dfs(self, start, S, result, father_subsets):
        result.append(father_subsets)
        for i in range(start, len(S)):
            self.dfs(i+1, S, result, father_subsets+[S[i]])

    def subsets(self, S):
        # none case
        if S is None:
            return []
        # deep first search
        result = []
        self.dfs(0, sorted(S), result, [])
        return result


class Solve:
    def dfs(self, start, S, result, subset):
        result.append(subset)
        for i in range(start, len(S)):
            self.dfs(i+1,S,result,subset +[S[i]])

    def subset(self,S):
        if S is None:
            return []
        result = []
        self.dfs(0, S, result, [])
        return result


if __name__ == "__main__":
    s = Solution()
    result = s.subsets([1,2,3,4])
    print(result)
    print(len(result))



