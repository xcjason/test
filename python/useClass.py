class TestClass(object):
	def __init__(self, count):
		self.count = count

	def __enter__(self):
		print 'enter function'
		return self

	def getCount(self):
		return self.count

	def __exit__(self, exceptionType, exceptionValue, traceBack):
		print 'object destroyed'


with TestClass(20) as sample:
	print sample
	print sample.getCount()