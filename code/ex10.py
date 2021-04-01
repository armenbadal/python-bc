import unittest


def binarySearch(e, els):
    left = 0
    right = len(els) - 1
    while left < right:
        middle = (left + right) // 2

        if els[middle] == e:
            return middle
        
        if els[middle] > e:
            right = middle - 1
        elif els[middle] < e:
            left = middle + 1
    
    return -1



def binarySearchRec(e, els, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    if els[middle] == e:
        return middle

    if els[middle] > e:
        return binarySearchRec(e, els, left, middle -1)
    elif els[middle] < e:
        return binarySearchRec(e, els, middle + 1, right)
    


#
#
els = [0, 1, 2, 3, 4, 6, 7, 8, 9]

#k = binarySearch(7, els)
#assert k == 6
#
#k = binarySearch(2, els)
#assert k == 2
#
#k = binarySearch(5, els)
#assert k == -1


k = binarySearchRec(7, els, 0, len(els) - 1)
assert k == 6

k = binarySearchRec(2, els, 0, len(els) - 1)
assert k == 2

k = binarySearchRec(5, els, 0, len(els) - 1)
assert k == -1
