def getStat(guess, solution):
	solutionMask = 0
	res = [0, 0]
	for i in xrange(4):
		solutionMask |= 1 << ord(solution[i]) - ord('A')
	for i in xrange(4):
		if guess[i] == solution[i]: res[0] += 1
		elif (solutionMask & (1 << (ord(guess[i]) - ord('A')))) >= 1: 
			res[1] += 1
	return res


print getStat('YRGB', 'RGGB')
print getStat('GGGB', 'RGGB')