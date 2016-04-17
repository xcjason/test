__author__ = 'jason'

from collections import deque
import pdb


def friend_circle(friends):
    group_num = 0
    visited = set()
    queue = deque()
    for i in xrange(len(friends)):
        if i not in visited:
            queue.append(i)
            while queue:
                cur = queue.popleft()
                visited.add(cur)
                cur_friend = [v for v, x in enumerate(friends[cur]) if x == 'Y' and v not in visited]
                queue.extend(cur_friend)
            group_num += 1
            queue = deque()
    return group_num


def longest_chain(pool):
    if not pool:
        return 0
    str_set = set(pool)
    pool.sort(key=lambda x: len(x), reverse=True)
    res = 0
    for s in pool:
        if len(s) <= res:
            return res + 1
        res_for_s = recur_string_chain(s, 0, str_set)
        res = max(res, res_for_s)
    return res + 1


def recur_string_chain(left, length, str_set):
    if not left:
        return length
    record = []
    for i in xrange(len(left)):
        shorter_str = left[:i] + left[i + 1:]
        if shorter_str in str_set:
            record.append(recur_string_chain(shorter_str, length + 1, str_set))
    if record:
        return max(record)
    else:
        return length

if __name__ == '__main__':
    L = ['6', 'a', 'b', 'ba', 'bca', 'bda', 'bdca']
    # print longest_chain(L)
    friends = [['Y', 'Y', 'N', 'N'], ['Y', 'Y', 'Y', 'N'], ['N', 'Y', 'Y', 'N'], ['N', 'N', 'N', 'Y']]
    print friend_circle(friends)
