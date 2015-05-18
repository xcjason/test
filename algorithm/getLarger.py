def getLarger(x, y):
    l = [x, y]
    return l[(x - y) >> 31]

if __name__ == '__main__':
    print getLarger(5, 10)
    print getLarger(10, 5)
    print getLarger(3, 5)


