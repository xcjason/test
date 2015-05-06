def initial(s, t):
	lenS, lenT = len(s), len(t)
	prev = [(s.index(t[0]), 1)]
	for i in xrange(1, lenS):
	    if t[0] == s[i]:
	        prev.append((i, prev[-1][1] + 1))
	return prev

print initial('rabcab', 'rab')
print initial('rabcarbrr', 'rab')