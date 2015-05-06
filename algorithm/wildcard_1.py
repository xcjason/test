class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
    	sLoc, pLoc, ss, star = 0, 0, 0, -1
    	lenS, lenP = len(s), len(p)
    	while sLoc < lenS:
    		if pLoc < lenP and (s[sLoc] == p[pLoc] or p[pLoc] == '?'):
    			sLoc += 1; pLoc += 1
    			continue
    		if pLoc < lenP and p[pLoc] == '*':
    			ss = sLoc; star = pLoc; pLoc += 1
    			continue
    		if star != -1:
    			ss += 1; sLoc = ss; pLoc = star + 1; 
    			continue
    		return False
    	for c in p[pLoc:]:
    		if c != '*': return False
    	return True


sol = Solution()
print sol.isMatch('aa', '*')
print sol.isMatch('aa', 'aaa')
print sol.isMatch('ab', '*?')
print sol.isMatch('aab', 'c*b*a')
print sol.isMatch('abefcdgiescdfimde', 'ab*cd?i*de')
print sol.isMatch('babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb', 'b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a')