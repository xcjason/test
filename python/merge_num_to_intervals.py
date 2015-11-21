def merge(L):
    if len(L) <= 1:
        return L
    start = end = 0
    cur = 1
    res = []
    while cur < len(L):
        if L[cur] - L[end] > 1:
            if L[end] - L[start] == 0:
                res.append(str(L[end]))
            else:
                res.append(str(L[start]) + '-' + str(L[end]))
            start = end = cur
        else:
            end = cur
        cur += 1

    if L[end] - L[start] == 0:
        res.append(str(L[end]))
    else:
        res.append(str(L[start]) + '-' + str(L[end]))
    return res

def main():
    l1 = [1, 2, 3, 4, 6]
    l2 = [1, 3, 5, 7]
    l3 = [1, 3, 4, 5, 7, 9, 11]
    print merge(l1)
    print merge(l2)
    print merge(l3)

if __name__ == '__main__':
    main()
