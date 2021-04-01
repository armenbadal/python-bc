import random
import turtle

def indexOf(els):
    mi = 0
    me = els[mi]
    for j in range(len(els)):
        if els[j] < me:
            me = els[j]
            mi = j
    return mi


def selectionSort(els):
    for i in range(len(els)):
        mi = i + indexOf(els[i:])
        els[i], els[mi] = els[mi], els[i]
    return els



turtle.speed('fast')

def drawPoints(els):
    pass
