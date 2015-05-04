def printOut(x, st='hello', *args):
	print 'x:', x
	print 'st', st
	for i in args:
		print i


def fun():
	return False

printOut('1', '2', '3', 7, fun)
printOut([3, 4, 5], 'this', 7, 2, 3)

def tryArgu(x, **kwargs):
	print 'x:', x
	for k in kwargs:
		print k, kwargs[k]

tryArgu(34, i=1, j=2, k=3)