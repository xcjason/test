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
    print("deco1")  
    return func  
  
def deco2(func):  
    print("deco2")  
    return func  
 
@deco2  
@deco1  
def foo():  
    print("foo")  
  
foo() 