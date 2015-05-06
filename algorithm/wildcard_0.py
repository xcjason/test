class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        if p == '': return s == p
        return self.recur(s, p)
    
    def recur(self, s, p):
        if s == '':
            return True if p == '' or p == '*' or p == '?' else False
        if p == '': return True if s == '' else False
        if p[0] == '?': return self.recur(s[1:], p[1:])
        if p[0] == '*':
            if len(p) == 1: return True
            if p[1] == '*': return self.recur(s, p[1:])
            if p[1] == '?':
                for i in range(len(s)):
                    if self.recur(s[i:], p[1:]): return True
                return False
            L = self.getIndex(s, p[1])
            for i in L:
                if self.recur(s[i:], p[1:]): return True
            return False
        if p[0] == s[0]: return self.recur(s[1:], p[1:])
        return False

    def getIndex(self, s, c):
        res = []
        for i, v in enumerate(s):
            if v == c: res.append(i)
        return res

sol = Solution()
print sol.isMatch('aa', '*')
print sol.isMatch('aa', 'aaa')
print sol.isMatch('ab', '*?')
print sol.isMatch('aab', 'c*b*a')
print sol.isMatch('abefcdgiescdfimde', 'ab*cd?i*de')
print sol.isMatch('babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb', 'b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a')