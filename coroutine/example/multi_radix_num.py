import pdb
from itertools import product
from operator import mul
from functools import reduce

# =============Base line solution===================

def multiradix_0_product(M):
    return product(*(range(x) for x in M))

# =============Solution 1===================

def multiradix_1_counting(M):
    n = len(M)
    a = [0] * n
    last = reduce(mul, M, 1)
    for x in range(last):
        yield number_to_multiradix(M, x, a)


def number_to_multiradix(M, x, a):
    n = len(M)
    for i in range(1, n + 1):
        x, a[-i] = divmod(x, M[-i])
    return a


# =============Last solution===================

def multiradix_3_coroutine(M):
    n = len(M)
    a = [0] * n
    lead = troll(M, a, n - 1)
    yield a
    while next(lead):
        yield a

def nobody():
    while True:
        yield False

def troll(M, a, i):
    previous = troll(M, a, i - 1) if i > 0 else nobody()
    while True:
        if a[i] == M[i] - 1:
            a[i] = 0
            yield next(previous)
        else:
            a[i] += 1
            yield True


if __name__ == '__main__':
    M = [3, 2, 4]
    # for i in multiradix_0_product(M):
    #     print i
    # for i in multiradix_1_counting(M):
    #     print i
    for i in multiradix_1_counting(M):
        print i
