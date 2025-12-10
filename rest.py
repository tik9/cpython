from pathlib import Path
import sys

home = str(Path.home())


def main():
    '''main'''
    # fib(2)
    isPrime(4,8)
    # palindrome()
    # mat_rev()
    # one_by_one(4)
    # print(home)
    # print(version())

def fib(nr):
    '''input: nr, e.g. 5
    output: fibonacci numbers until nr, e.g. 01123
    '''
    x1=0
    x2=1
    print(x1,x2, end=' ')
    for i in range(nr-2):
        x3=x1+x2
        x1=x2
        x2=x3
        print(x3,end=' ')

def isPrime(nr1,nr2):
    '''input: 2 numbers, e.g. 4 and 6
    output: check if numbers between two numbers are prime (yes) or not (no), here 'no'
    '''
    for nr in range(nr1,nr2+1):
        nrSquare=int(nr**0.5)
        for i in range(2,nrSquare+1):
            if nr%i==0:
                print(str(nr)+' no prime')
                break
            print(str(nr)+' = prime')


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
    12
    45
    
    b)size, here: 2
    output: change last column to first row, second last to second etc.
    25
    14
    '''

    input=[[1,2,3],[4,5,6],[7,8,9]]
    output=[]
    size=3
    for i in range(size -1,-1,-1):
        inner=[]
        for j in range(0,size):
            inner.append(input[j][i])
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
