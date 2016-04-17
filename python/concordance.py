__author__ = 'jason'
import collections
import json
import re
import sys

SPECIAL_CASES = {
    'Mr.': 'Mr ',
    'Ms.': 'Ms ',
    'Mrs.': 'Mrs ',
    'Dr.': 'Dr '
}

SPECIAL_CHARACTERS = '()[]{}"'


def _clean_line(line):
    """
    Remove special characters (parenthesis, quotes, etc.) in one single line
    :param line: string
    :return:string without special characters
    """
    for k, v in SPECIAL_CASES.iteritems():
        line = line.replace(k, v)
    for c in SPECIAL_CHARACTERS:
        line = line.replace(c, ' ')
    return line


def _aggregate_result(result):
    """
    :param result: aggregate concordance
    :return: None.
    """
    for word, line_numbers in result.iteritems():
        result[word] = {len(line_numbers): line_numbers}


def get_concordance(file_name):
    """
    :param file_name: file name of the document needs to process
    :return: unsorted default dictionary using word as key, {<count>: <list of sentence number>} as value
    """
    concordance = collections.defaultdict(list)
    sentence_index = 1
    with open(file_name) as f:
        for line in f:  # put single line into memory
            if not line.strip():
                continue  # empty lines do not count
            line = _clean_line(line)
            sentences = re.split(r'[\.\?!]', line)
            for sentence in sentences:
                if not sentence.strip():  # empty sentences do not count
                    continue
                for word in sentence.strip().strip("'").split():
                    concordance[word.lower().strip().strip(",").strip("'")].append(sentence_index)
                sentence_index += 1
    _aggregate_result(concordance)
    return concordance


def main():
    if len(sys.argv) != 2:
        raise RuntimeError('Please provide SINGLE file name for which needs to be processed')
    file_name = sys.argv[1]
    concordance = get_concordance(file_name)
    return json.dumps(concordance, sort_keys=True)  # json module does the sorting


if __name__ == '__main__':
    main()
