"""
[["X","E","X","E","X","E"],
 ["E","X","O","X","O","X"],
 ["X","O","X","E","X","O"],
 ["E","X","E","X","E","X"]]

"""

# Option 1: DFS
class Solution(object):
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        if not board or len(board) == 0:
            return
        self.l_row = len(board)
        self.l_col = len(board[0])
        if self.l_col <= 2 or self.l_row <= 2: # if size 2 * 2
            return

        for r in range(self.l_row): # first row and last row contains 'O then mark
            self.dfs(board, r, 0)
            self.dfs(board, r, self.l_col - 1)
        for c in range(self.l_col):# first col and last col contains 'O then mark
            self.dfs(board, 0, c)
            self.dfs(board, self.l_row - 1, c)

        for r in range(self.l_row): # check if 'O' -> 'X', then check if 'E' -> '0'
            for c in range(self.l_col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'E':
                    board[r][c] = 'O'

    def dfs(self, board, r, c): # DFS only check the boarder 'O', leave the middle 'O' untouched
        if 0 <= r < self.l_row and 0 <= c < self.l_col and board[r][c] == 'O':
            board[r][c] = 'E'
            self.dfs(board, r + 1, c)
            self.dfs(board, r - 1, c)
            self.dfs(board, r, c + 1)
            self.dfs(board, r, c - 1)
