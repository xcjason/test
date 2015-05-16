class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if board == []: return
        if board[0] == []: return
        m, n = len(board), len(board[0])
        for i in xrange(n):
            if board[0][i] == 'O': self.recur(0, i, board)
            if board[m - 1][i] == 'O': self.recur(m - 1, i, board)
        for i in xrange(m):
            if board[i][0] == 'O': self.recur(i, 0, board)
            if board[i][n - 1] == 'O': self.recur(i, n - 1, board)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '$': board[i][j] = 'O'
    
    def recur(self, i, j, board):
        m, n = len(board), len(board[0])
        board[i][j] = '$'
        if i > 0 and board[i - 1][j] == 'O': self.recur(i - 1, j, board)
        if i < m - 1 and board[i + 1][j] == 'O': self.recur(i + 1, j, board)
        if j > 0 and board[i][j - 1] == 'O': self.recur(i, j - 1, board)
        if j < n - 1 and board[i][j + 1] == 'O': self.recur(i, j + 1, board)


sol = Solution()
board1 = [['O', 'O', 'O'], ['O', 'X', 'O'], ['O', 'O', 'O']]
sol.solve(board1)
print board1

board2 = [['O', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', 'O']]
sol.solve(board2)
print board2