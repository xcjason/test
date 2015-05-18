class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        if n == 0: return []
        sol = []
        self.recur([-1] * n, 0, sol)
        res = []
        for s in sol:
            board = [['.'] * n for i in xrange(n)]
            for i in xrange(n):
                board[i][s[i]] = 'Q'
                board[i] = ''.join(board[i])
            res.append(board)
        return res
    
    def recur(self, rec, cur, sol):
    	dim = len(rec)
        if cur == dim: sol.append(rec); return
        for i in xrange(dim):
            for j in xrange(cur):
                if rec[j] == i: break
                if abs(rec[j] - i) == abs(cur - j): break
            else:
                next = rec[:]
                next[cur] = i
                self.recur(next, cur + 1, sol)
        		

if __name__ == '__main__':
	sol = Solution()
	print sol.solveNQueens(4)
