def salesgirl(method):
    def serve(*args):
        print "Salesgirl:Hello, what do you want?", method.__name__
        method(*args)
    return serve
   

def try_this_shirt(size):
    if size < 35:
        print "I: %d inches is to small to me" %(size)
    else:
        print "I:%d inches is just enough" %(size)
#try_this_shirt(38)

def deco1(func):  
    print 'deco1'
    def wrapper(arg):
        return func() + '|deco1'
    return wrapper
  
def deco2(func):
    print 'deco2'
    def wrapper(arg):
        return func(arg) + '|deco2'
    return wrapper

@deco2
def foo(name):  
    print 'foo'
    return 'hello ' + name
  
print foo('Jimmy') 

myFoo = deco2(foo)
print myFoo('Kate')
