from urlparse import urlparse
import sys


def getEpuratedDomains(fileName):
    with open(fileName, 'r') as fp:
        lines = (l for i, l in enumerate(fp) if i > 1)
        urls = (l.split('\t')[1][1:-1] for l in lines if l.split('\t')[1])
        domains = (urlparse(url).netloc for url in urls)
        return list(set(domains))


if __name__ == '__main__':
    try:
        fName = sys.argv[1]
    except IndexError:
        print 'usage: python tsvparse.py <file>'
        sys.exit(1)
    for d in getEpuratedDomains(fName):
        print d