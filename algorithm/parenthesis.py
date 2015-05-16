class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0: return []
        result = set([])
        self.recur('(', n - 1, n, result)
        return result
    
    def recur(self, tmp, left, right, result):
        if left == right == 0: result.add(tmp); return
        if left == 0: result.add(tmp + ')' * right); return
        if left > right: return
        self.recur(tmp + '(', left - 1, right, result)
        self.recur(tmp + ')', left, right - 1, result)

if __name__ == '__main__':
    sol = Solution()
    print sol.generateParenthesis(3)
