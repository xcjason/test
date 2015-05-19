def printOut(x, st='hello', *args):
	print 'x:', x
	print 'st', st
	print 'args:', args

def fun():
	return False

def tryArgu(x, **kwargs):
	print 'x:', x
	print 'kwargs: ', kwargs

def anotherTryArg(x, st='sky', *args, **kwargs):
	print 'args: ', args
	print 'kwargs: ', kwargs


if __name__ == '__main__':
	printOut('1', '2', '3', 7, fun)
	print '======================'
	printOut([3, 4, 5], 'this', 7, 2, 3)
	print '======================'
	tryArgu(34, i=1, j=2, k=3)
	print '======================'
	anotherTryArg(67, 'this', 'hello', 'moon', a=5, b=7, c=0)