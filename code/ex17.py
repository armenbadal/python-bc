# Ցուցակի ցիկլիկ տեղաշարժ դեպի աջ

# Պարզագույն լուծումը
def rotateRight(els, n):
    return els[-n:] + els[0:-n]


def rotateRightClassic(els, n):
    els = reverseList(els, 0, n)
    els = reverseList(els, n, len(els))
    els = reverseList(els, 0, len(els))
    return els

def reverseList(els, b, e):
    while b < e:
        esl[b], els[e] = els[e], els[b]
        b += 1
        e -= 1
    return els

def reverseListRec(els):
    if len(els) <= 1:
        return els
    return reverseListRec(els[1:]) + [els[0]]

