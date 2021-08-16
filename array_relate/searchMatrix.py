# -*- coding:utf-8  -*-
class Solution(object):

    @staticmethod
    def search_matrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        row = len(matrix)
        target_row = []
        for i in range(row - 1, -1, -1):
            if target > matrix[i][-1]:
                return False
            elif target >= matrix[i][0]:
                target_row = matrix[i]
                break
            elif target < matrix[i][0] and target > matrix[i - 1][0]:
                target_row = matrix[i - 1]
                break
            else:
                continue

        return target in target_row

    @staticmethod
    def search_matrix_(self, matrix, target):
        if matrix == [] or matrix == [[]]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        i, j = row-1, 0
        while i >= 0 and j < col:
            if target == matrix[i][j]:
                return True
            if target > matrix[i][j]:
                j += 1
            else:
                i -= 1
        return False

    def searchMatrix(self, matrix, target):
        start, end = 0, len(matrix)
        loc = 0

        # 二分查找目标行
        while start < end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                loc = mid
                start = mid + 1
            else:
                end = mid

        l, r = 0, len(matrix[0]) - 1

        # 二分查找目标行的全部数据
        while l <= r:
            mid = (l + r) // 2
            if matrix[loc][mid] == target:
                return True
            elif matrix[loc][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 30
    print(s.search_matrix(matrix, target))