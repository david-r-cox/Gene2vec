#!/usr/bin/python2.7
# David Cox 2016
from os import path, listdir
from sys import argv

'''
Prints all n-grams in a file. 
Suggested usage is to redirect output to a file.
'''

WINDOW_SIZE = 601

def argcheck():
    if len(argv) != 2:
        print('./word_gen.py <input directory>')
        exit(1)
    if not path.isdir(argv[1]):
        print('Input directory not found or does not exist.')
        exit(1)
    return

def window(data):
    for i in xrange(len(data) - WINDOW_SIZE): yield data[i:i+WINDOW_SIZE]


def main():
    argcheck()
    path = lambda x : argv[1] + '/' + x
    read = lambda x : ''.join(open(x, 'r').read().split()).upper()

    for f in listdir(argv[1]):
        data = read(path(f))
        for n in window(data):
            print n,


if __name__ == "__main__":
    main()
