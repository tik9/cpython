import os
from pathlib import Path

home = str(Path.home())

print(home)

file_ = os.path.join(home, '')


def main():
    str = ''
    # 100101
    str = bingap(37)
    str=count_div(1, 2000, 100)
    print(str)


def bingap(N):
    
    bin_representation = bin(N)[2:]
    max_gap = 0
    gap_counter = 0
    gap_started = False
    for symbol in bin_representation:
        if symbol == '1':
            if gap_counter > max_gap:
                max_gap = gap_counter
            gap_counter = 0
            gap_started = True
        elif gap_started:
            gap_counter += 1
    return max_gap

def count_div(A, B, K):
    '''
    Returns the number of integers within the range [A..B] that are divisible by K.
    Used generators to save memory on large amounts of data.
    '''
    divs_count = 0
    for x in xrange(A, B + 1):
        if (x % K) == 0:
            divs_count += 1
    return divs_count

if __name__ == "__main__":
    main()
