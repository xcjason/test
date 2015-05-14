def getPrime(n):
    n += 1
    rec = [True] * n
    full = range(n)
    result = []
    for num in xrange(2, int(n ** 0.5)):
        if not rec[num]: continue
        later = num * 2
        while later <= n - 1:
            rec[later] = False
            later += num
    result = [full[i] for i in xrange(n) if rec[i]]
    return result[2:]


if __name__ == '__main__':
    print getPrime(100)
    print getPrime(200)
