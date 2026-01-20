
def main():
    '''main'''

    numbers = [3, 1, 4]
    # max_num = find_max(numbers)
    # print(f"The maximum number is: {max_num}")

    fizz_buzz(15)
    
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

def find_max(numbers):
    '''find max in list'''
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

if __name__ == '__main__':
    main()
