import pdb


def enum(*sequential, **named):
    """
    :param sequential:
    :param names:
    :return: a fake enumerated type in python
    """
    enums = dict(zip(sequential, range(len(sequential))), **named)
    pdb.set_trace()
    return type('Enum', (), enums)

if __name__ == '__main__':
    tags = enum('READY', 'DONE', 'EXIT', 'START')
