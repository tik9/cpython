from pathlib import Path
import sys

home = str(Path.home())


def main():
    '''main'''
    isPrime()
    # palindrome()
    # mat=mat_rev_short()
    # one_by_one(4)
    # print(home)
    # print(version())

def isPrime():
    '''input: number, e.g. 4
    output: check if number is prime (yes) or not (no), here 'no'
    '''
    nr=7
    nrSquare=int(nr**0.5)
    for i in range(2,nrSquare+1):
        if nr%i==0:
            print('no')
            return
    print('yes')


def palindrome():
    '''input: 'anna', 'hanna'
    output: check if first and last chars are equal; if all are equal: yes, othwerwise no
    '''
    str='anna'
    str='hanna'
    lenStr=len(str)
    for i in range(int(lenStr/2)):
        if str[i]!=str[lenStr-1]:
            print('no')
            return
        lenStr-=1
    print('yes')


def mat_rev_short():
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    size = len(input_matrix)  # Größe dynamisch ermitteln
    output_matrix = [[input_matrix[j][i] for j in range(size)] for i in range(size - 1, -1, -1)]

    for row in output_matrix:
        print(*row) # Verwendung von * zum entpacken der Liste für print

def mat_rev():
    '''Given: a)input: 
    123
    456
    789
    b)size, here: 2
    output: change last column to first row, second last to second etc.
    369
    258
    147
    '''

    input=[[1,2,3],[4,5,6],[7,8,9]]
    output=[]
    size=3
    for i in range(size -1,-1,-1):
        inner=[]
        for j in range(0,size):
            last=input[j][i]
            inner.append(last)
        output.append(inner)
    
    for i in range(0,size):
        for j in range(0,size):
            print(output[i][j],end=' ')
        print()

    return output

def one_by_one(x):
    '''
    multiply first row with first col and return matrix
    1 2 3
    2 4 6
    3 6 9
    '''
    y=x+1
    for i in range (1,y):
        print(i, end=' ')
    print()
    for i in range (2,y):
        print(i,end=' ')
        for j in range(2,y):
            print(i*j,end=' ')
        print()

    # return 'ok'

def version():
    '''version'''
    return [sys.version_info, sys.version_info.major]


if __name__ == "__main__":
    main()
