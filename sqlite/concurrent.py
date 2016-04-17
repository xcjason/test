__author__ = 'jason'
from multiprocessing import Pool
from os import listdir
from os.path import isfile, join
import sqlite3
import sys

DB_NAME = 'concurrent.sqlite'


def save_file_into_sqlite(file_name):
    conn = sqlite3.connect(DB_NAME)
    with open(file_name) as f:
        for line in f.readlines():
            with conn:
                conn.execute("INSERT INTO test_table (line) VALUES (?)", (line.strip().decode('utf-8'),))


def main():
    conn = sqlite3.connect(DB_NAME)
    cs = conn.cursor()
    cs.execute('''CREATE TABLE IF NOT EXISTS test_table(
                  id integer PRIMARY KEY AUTOINCREMENT,
                  line text); ''')
    file_dir = sys.argv[1]
    files = [join(file_dir, f) for f in listdir(file_dir) if isfile(join(file_dir, f))]
    pool = Pool(len(files))
    # pool = Pool(1)
    import pdb; pdb.set_trace()
    pool.map(save_file_into_sqlite, files)
    # save_file_into_sqlite(files[0])

if __name__ == "__main__":
    main()
