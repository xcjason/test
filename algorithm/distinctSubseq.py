class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        lenS, lenT = len(s), len(t)
        
        prev = [(s.index(t[0]))]
        for i in xrange(1, lenS):
        	if t[0] == s[i]:
        		prev.append((i, prev[-1][1] + 1))

		for k in xrange(lenT):
			cur = []
			for i, v in prev:
				count = 0
				for j in xrange(i+1, lenS):
					if t[k] == s[j]:
						count += 1
						cur.append((j, v + count - 1))
