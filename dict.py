import sys
from CoreServices import DictionaryServices


searchword = ''
if sys.argv[1:]:
    searchword = sys.argv[1]


def main():
    dict()


def dict():
    wordrange = (0, len(searchword))
    dictresult = DictionaryServices.DCSCopyTextDefinition(
        None, searchword, wordrange)
    if not dictresult:
        print(searchword+" not found")
    else:
        print(dictresult)


if __name__ == '__main__':
    main()
