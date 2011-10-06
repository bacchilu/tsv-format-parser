from urlparse import urlparse
import sys


def lines(fp):
    return (l for i, l in enumerate(fp) if i > 1)


def urls(fp):
    return (l.split('\t')[1][1:-1] for l in lines(fp) if l.split('\t')[1])


def domains(fp):
    return (urlparse(url).netloc for url in urls(fp))


def getEpuratedDomains(fileName):
    with open(fileName, 'r') as fp:
        return list(set(domains(fp)))


if __name__ == '__main__':
    try:
        fName = sys.argv[1]
    except IndexError:
        print 'usage: python tsvparse.py <file>'
        sys.exit(1)
    for d in getEpuratedDomains(fName):
        print d