__author__ = 'jason'
import timeit

def intuitive_way(key_num, list_len):
    data = {}
    for i in xrange(key_num):
        for j in xrange(list_len):
            if i not in data:
                data[i] = [str(j)]
            else:
                data[i].append(str(j))

def use_set_default(key_num, list_len):
    data = {}
    for i in xrange(key_num):
        for j in xrange(list_len):
            data.setdefault(i, []).append(str(j))

if __name__ == '__main__':
    print(timeit.timeit(stmt='intuitive_way(100, 1000)', setup='from __main__ import intuitive_way', number=300))
    print(timeit.timeit(stmt='use_set_default(100, 1000)', setup='from __main__ import use_set_default', number=300))
