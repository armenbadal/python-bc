
def partition(els):
    pix = len(els) // 2
    pivot = els[pix]

    left = 0
    right = len(els) - 1
    while left < right:
        while els[left] < pivot:
            left += 1

        while els[right] > pivot:
            right -= 1

        if left <= right:
            els[left], els[right] = els[right], els[left]
            left += 1
            right -= 1

    return els


els = [44, 55, 12, 42, 94, 16, 18, 67]
els = partition(els)
print(els)
