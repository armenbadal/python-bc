
def greater(a, b):
    return a > b

def lesser(a, b):
    return a < b

def equal(a, b):
    return a == b

def indexOf(els, compare):
    mi = 0
    me = els[mi]
    for j in range(len(els)):
        if compare(els[j], me):
            me = els[j]
            mi = j
    return mi

def selectionSort(els, compare):
    for i in range(len(els)):
        mi = i + indexOf(els[i:], compare)
        els[i], els[mi] = els[mi], els[i]
    return els


def diditCount(a, b):
    return len(str(a)) < len(str(b))




els = [10, 27773, 10000, 5, 45, 217, 14, 96, 7, 7777, 47, 89, 71, 0, 84, 55]
print(els)
els = selectionSort(els, diditCount)
els = selectionSort(els, lesser)
print(els)
