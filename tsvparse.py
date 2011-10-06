from urlparse import urlparse
import sys
import os
import glob


def getDomains(fileName):
    with open(fileName, 'r') as fp:
        lines = (l for i, l in enumerate(fp) if i > 1)
        urls = (l.split('\t')[1][1:-1] for l in lines if l.split('\t')[1])
        domains = (urlparse(url).netloc for url in urls)
        return set(domains)


def prettyPrint(fName, values):
    print '=============' + fName + '============='
    for e in values:
        print e


if __name__ == '__main__':
    try:
        p = sys.argv[1]
    except IndexError:
        print 'usage: python tsvparse.py <filepath or directorypath>'
        sys.exit(1)
    if os.path.isfile(p):
        prettyPrint(p, getDomains(p))
    if os.path.isdir(p):
        for fName in glob.iglob(os.path.join(p, '*.tsv')):
            prettyPrint(fName, getDomains(fName))