import sys
from CoreServices import DictionaryServices


def main():
    try:
        searchword = sys.argv[1]
    except IndexError:
        print('enter term')
        sys.exit()
    wordrange = (0, len(searchword))
    dictresult = DictionaryServices.DCSCopyTextDefinition(
        None, searchword, wordrange)
    if not dictresult:
        print(searchword+" not found")
    else:
        print(dictresult)


if __name__ == '__main__':
    main()
