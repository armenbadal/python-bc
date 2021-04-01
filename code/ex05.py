
def isSorted(els):
    i = 0
    while i < len(els) - 1:
        if els[i] > els[i+1]:
            return False
        i += 1
    return True


def bubbleSort(els):
    for k in range(0, len(els)):
        for i in range(1, len(els)):
            if els[i-1] > els[i]:
                els[i-1], els[i] = els[i], els[i-1]

    return els







#els = [9, 1, 5, 2, 8, 3, 7, 3, 3, 1, 4, 5, 0, 6]
els = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
els = bubbleSort(els)
print(els)
