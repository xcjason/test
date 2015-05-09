import string

def readFile(fileName):
    f = open(fileName)
    content = f.read()
    words = set([])
    for line in content.splitlines():
        for word in map(string.lower, line.split()):
            words.add(word)
    return words

if __name__ == '__main__':
    print readFile('textFile.txt')
