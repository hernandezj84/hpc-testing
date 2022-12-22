import itertools
numbers = [3, 2, 9]
# numbers = [6, 68, 61]
# numbers = [4, 42, 46, 427, 465]
# numbers = [5, 52, 57, 517, 532, 569, 581]
# numbers = [3, 9, 5, 9, 7, 1]
# 3, 9, 5, 9, 7


def old(a):
    total = []
    list_numbers = list(itertools.permutations(a))

    for x in list_numbers:
        n = [str(x) for x in x]
        s = int("".join(n))
        total.append(s)

    return max(total)

def old_database(a):
    list_numbers = list(itertools.permutations(a))
    return 0

def isGreater(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    r = False
    if ab > ba:
        r = True
    return r

def largest_number(a):
    for n in range(len(a)-1, 0, -1):
        for i in range(n):
            if isGreater(a[i], a[i + 1]):
                a[i], a[i + 1]  = a[i + 1], a[i]
    a.reverse()
    str_numbers = ''.join(map(str, a))
    return int(str_numbers)
