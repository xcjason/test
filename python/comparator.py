import unittest

def compare(x, y):
	X = getList(x)
	Y = getList(y)
	l = min(len(X), len(Y))
	for i in xrange(l):
		if X[i] == Y[i]: continue
		if X[i].isdigit(): return int(X[i]) - int(Y[i])
		if X[i] < Y[i]: return -1
		else: return 1
	if len(X) < len(Y): return -1
	elif len(X) > len(Y): return 1
	return 0

def getList(x):
	res = []
	tmp = x[0]
	for i in xrange(1, len(x)):
		if x[i].isdigit() ^ x[i - 1].isdigit(): # different
			res.append(tmp)
			tmp = x[i]
		else:
			tmp += x[i]
	if tmp: return res + [tmp]

class ComparatorTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(getList('12e5'), ['12', 'e', '5'])
        self.assertEqual(getList('1e5nj789'), ['1', 'e', '5', 'nj', '789'])

    def testCompare(self):
    	self.assertEqual(compare('12e5', '12e3'), 2)
    	self.assertEqual(compare('1a5', '1e3'), -1)
    	self.assertEqual(compare('1a5', '1a5'), 0)

    def testSort(self):
    	L = ['1a2', '1a10', '1a8', '1a1']
    	self.assertEqual(sorted(L, cmp=compare), ['1a1', '1a2', '1a8', '1a10'])
    	L = ['1e2', '1a10', '1a8', '1a1']
    	self.assertEqual(sorted(L, cmp=compare), ['1a1', '1a8', '1a10', '1e2'])
    	L = ['1e2', '1a10', '1e2k', '1a8', '1a1']
    	self.assertEqual(sorted(L, cmp=compare), ['1a1', '1a8', '1a10', '1e2', '1e2k'])

if __name__ == '__main__':
    unittest.main()
