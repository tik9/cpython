
def algo(list, val):
    lo = 0
    hi = len(list)-1
    mid = 0

    while lo <= hi:
        mid = (lo+hi)//2
        if list[mid] == val:
            return mid
        if list[mid] > val:
            hi = mid-1
        else:
            lo = mid+1
    return -mid-1


print(algo([1, 2, 3, 5], 1))

# print(algo([1, 2, 3, 4], 2))
# print(algo([1, 2, 3, 4, 5], 1))


def durchschnitt(list):
    sum = 0
    for elem in list:
        sum += elem
    avg = sum/len(list)
    return avg


def palindrom(str):
    for idx, ele in enumerate(str):
        # if str[-1] == str[0]:
        # print('equal')
        if str[idx] != str[len(str)-idx-1]:
            return False
    return True

# print(durchschnitt([1, 3, 2]))


# print(palindrom('otto1'))
