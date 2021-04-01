
def isArmenianLetter(c):
    return c.isalpha() and (c >= 'Ա' and c <= 'Ֆ') or (c >= 'ա' and c <= 'ֆ') or c == 'և'

def countLettersFromFile(name):
    freq = {}

    f = open(name, 'r', encoding='utf-8')
    for line in f:
        for c in [c.lower() for c in line if isArmenianLetter(c)]:
            freq[c] = freq.get(c, 0) + 1
    f.close()

    return freq

def createFrequencyFile(name, freq):
    f = open(name, 'w', encoding='utf-8')
    for e in freq:
        f.write(e[0])
        f.write(' ')
        f.write(str(e[1]))
        f.write('\n')
    f.close()

def sortByFreq(freq):
    w = []
    for f in freq:
        w.append((f, freq[f]))
    w.sort(reverse=True, key=lambda x: x[1])
    return w


freq = countLettersFromFile('idiot.mw')
freq = sortByFreq(freq)
createFrequencyFile('a0.txt', freq)
