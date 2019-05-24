# -*- coding:utf-8 -*-


class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, 0, i, j, visited):
                    return True
        return False

    def dfs(self,board, word, index, row_index, col_index, visited):
        if index == len(word):
            return True
        if row_index < 0 or col_index < 0 or row_index >= len(board) or col_index >= len(board[0]):
            return False
        if visited[row_index][col_index]:
            return False
        if board[row_index][col_index] != word[index]:
            return False
        visited[row_index][col_index] = True
        res = self.dfs(board, word, index + 1, row_index - 1, col_index, visited) or self.dfs(board, word, index + 1, row_index + 1, col_index,visited) or self.dfs(board, word, index + 1,row_index,col_index + 1, visited) or self.dfs(board, word, index + 1, row_index, col_index - 1, visited)
        visited[row_index][col_index] = False
        return res


if __name__ == "__main__":
    s = Solution()
    board = [['A', 'B', 'C', 'E'],  ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "ABCCED"
    res = s.exist(board, word)
    print(res)