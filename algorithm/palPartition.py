class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        lenS = len(s)
        rec = [[0] * lenS for i in xrange(lenS)]
        for j in xrange(lenS):
            for i in reversed(xrange(j + 1)):
                if s[i] == s[j] and (j - i <= 1 or rec[i + 1][j - 1]):
                    rec[i][j] = 1
        result = []
        print rec
        self.recur(0, s, [], rec, result)
        return result
    
    def recur(self, start, s, tmp, rec, result):
        if start == len(s): 
            result.append(tmp); return
        for i in xrange(start, len(s)):
            if rec[start][i]:
                self.recur(i + 1, s, tmp[:] + [s[start : i + 1]], rec, result)


sol = Solution()
print sol.partition('a')