from pathlib import Path
import sys

home = str(Path.home())

def main():
    '''main'''
    input=[4,3,2,1]
    print(selection_sort(input))
    # print(home)

def selection_sort(input):
    new_list=input[:]
    n = len(new_list)
    for i in range(0,n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if new_list[j] < new_list[minIndex]:
                minIndex = j
        if minIndex != i:
            new_list[i], new_list[minIndex]= new_list[minIndex],new_list[i]
    return new_list

def insertion_sort(input):
    new_list=input[:]
    for i in range(1,len(new_list)):
        key = new_list[i]
        j = i - 1

        while j >= 0 and new_list[j] > key:
            new_list[j + 1] = new_list[j]
            j = j - 1

        new_list[j + 1] = key
    
    return new_list

def bubble_sort(input):
    new_list=input[:]
    
    size=len(new_list)
    for i in range(0,size-1):
        for j in range(0,size-i-1):
            if new_list[j]>new_list[j+1]:
                new_list[j],new_list[j+1]=new_list[j+1],new_list[j]
    return new_list


if __name__ == "__main__":
    main()
