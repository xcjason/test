import readFile
import pdb

print readFile.readFile('textFile.txt')


def test_read_file_1(file_name):
    content = []
    with open(file_name) as f:
        lines = f.readlines()
        pdb.set_trace()
        for line in lines:
            content.append(line)
    return ''.join(content)


def test_read_file_2(file_name):
    content = []
    with open(file_name) as f:
        tmp = f.readline()
        while tmp:
            content.append(tmp)
            tmp = f.readline()
    return ''.join(content)


if __name__ == '__main__':
    # print test_read_file_1('textFile.txt')
    print test_read_file_2('textFile.txt')