
def main():
    # print(1)
    # print(durchschnitt([1, 3, 2]))
    # print(palindrom('otto1'))
    # print(bin_search([1, 2, 3, 5], 1))
    # print(solution('abcabcabcabc'))
    # occurr2('abccbaabccba')
    # occurr3('wewe')
    # occurr4('wewet')

    # occurr4('a')
    # occurr4('aa')
    # occurr4('abcabc')
    # occurr4('abcabcabc')
    # occurr4('aaT')
    occurr4('ababT')
    # test()


def test():
    s = 'a'
    s = s[:-1]
    print(s)
    # print(len(s) % 2)
    # print((s+s).find(s, 1, -1))


def occurr4(s):
    i = (s+s).find(s, 1, -1)
    print(i)
    if (len(s) % 2 != 0):
        if (len(set(s)) == 1):
            # one odd char
            pattern: s[0]
            Divisions: str(len(s))
            return
        else:
            s = s[:-1]
            if len(set(s)) == 1:
                # pattern:s[0]
                # one extra char
                # Divisions:len(s)
                return
            elif i == -1:
                sub = s[0:len(set(s))]
                # pattern:sub
                # Divisions:str(s.count(sub))
                # extra chars
                return
            else:
                sub = s[:i]
                # pattern:sub
                # Divisions:s.count(sub)
                # odd chars
                return
    else:
        if len(set(s)) == 1:
            # pattern: (s[0])
            # Divisions: str(len(s))
            # one 'even' char
            return
        else:
            sub = s[:i]
            # pattern: sub
            # Divisions: str(s.count(sub))
            # even chars
            return


def occurr3(s):
    i = (s+s).find(s, 1, -1)
    sub = s[:i]
    # Sub 1: ', sub
    s2 = s
    s2 = s2[:-1]
    sets = set(s2)
    lenset = len(sets)
    # Sub 2: s2[0:lenset]


def occurr(s):
    sub = s[0:len(set(s))]
    return (sub, s.count(sub))


def occurr2(s):
    i = (s+s).find(s, 1, -1)
    sub = s[:i]
    print(i)


def bin_search(list, val):
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


def durchschnitt(list):
    sum = 0
    for elem in list:
        sum += elem
    avg = sum/len(list)
    return avg


def palindrom(str):
    for idx, ele in enumerate(str):
        # if str[-1] == str[0]:
        # equal')
        if str[idx] != str[len(str)-idx-1]:
            return False
    return True


if __name__ == '__main__':

    main()
