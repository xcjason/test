class MonkeyTest(object):
    def __init__(self):
        self.a = 0
        self.b = 0

    def add(self, x, y):
        return x + y
    
    @staticmethod
    def multi(x, y):
        return x * y

monkey = MonkeyTest()
monkey2 = MonkeyTest()
print monkey.add(16, 30)
print MonkeyTest.multi(4, 5)
lbd = lambda x, y: 2000
oldAdd = monkey.add
monkey.add = lbd
print 'after monkey patch: ', monkey.add(16, 30)
print 'another object: ', monkey2.add(16, 30)
monkey.add = oldAdd
print 'restore to old function: ', monkey.add(16, 30)
