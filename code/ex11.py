
import random

def minInx(els):
    mi = 0
    for i in range(len(els)):
        if els[mi] > els[i]:
            mi = i
    return mi


def selectionSort(els):
    for i in range(len(els)):
        mi = i + minInx(els[i:])
        els[i], els[mi] = els[mi], els[i]
    return els


def insertionSort(els):
    pass


es = [random.randint(0, 20) for i in range(20)]
print(es)

es = selectionSort(es)
print(es)
