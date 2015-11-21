__author__ = 'jason'
import os
import time

__MAX_THREAD = 4


def set_max_thread(thread_num):
    global __MAX_THREAD
    __MAX_THREAD = thread_num

def map(func, arg_list):

    pass

def main():
    def test_function(i):
        time.sleep(i)
        print 'finished sleeping for ' + str(i) + 'seconds'
    map(test_function, range(1, 16))

if __name__ == '__main__':
    main()
