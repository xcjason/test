def readFile(fileName):
    f = open(fileName)
    line = f.readline()
    while line:
        print map(lower, line.split(' '))
        line = f.readline()


readFile('textFile.txt')