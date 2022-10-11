'''translation from https://gist.github.com/lambdamusic/bdd56b25a5f547599f7f
see my comment in the gist - all pyobc pip packages needed
'''

import sys
# from CoreServices import DictionaryServices
from DictionaryServices import DCSCopyTextDefinition

searchword = ''
if sys.argv[1:]:
    searchword = sys.argv[1]


def main():
    '''main'''
    dicti()


def dicti():
    '''the translation'''
    wordrange = (0, len(searchword))
    dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
    if not dictresult:
        print(searchword+" not found")
    else:
        print(dictresult)


if __name__ == '__main__':
    main()