
def main():
    '''main'''
    numbers = [3, 1, 4]

    # fizz_buzz(15)
    # fib(2)
    # isPrime(4,8)
    # palindrome()
    # mat_rev()
    # one_by_one(4)
    two_sum_indices(nums=numbers,target=3)


def fib(nr):
    '''input: nr, e.g. 5
    output: fibonacci numbers until nr, e.g. 01123 for nr=5
    '''
    x1=0
    x2=1
    print(x1,x2, end=' ')
    for i in range(nr-2):
        x3=x1+x2
        x1=x2
        x2=x3
        print(x3,end=' ')

def find_max(numbers):
    '''find max in list'''
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def fizz_buzz(n):
    '''fizz buzz'''
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

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

def two_sum_indices(nums, target):
    """
    Indices of two numbers in list that add up to target
    Args: list of integers, target sum
    Returns: list with indices [index1, index2] of two numbers or None
    """
    # Key: number, Value: index
    num_map = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            print([num_map[complement], index])
        
        num_map[num] = index

    print(None)

if __name__ == '__main__':
    main()
