
def splitLineToWords(line):
    result = []
    word = ''
    for c in line:
        if c in ['՞', '՜', '՛']:
            continue
        c = c.lower()
        if c.isalpha():
            word += c.lower()
        else:
            if 0 != len(word):
                result.append(word)
                word = ''
    return result
        

def wordFrequency(fname):
    words = {}

    f = open(fname, 'r', encoding='utf-8')
    for line in f:
        ws = splitLineToWords(line)
        for w in ws:
            words[w] = words.get(w, 0) + 1
    f.close()

    return words


def maxUsed(words):
    mx = 0
    w = ''
    for k, v in words.items():
        print(k, '-->', v)
        if v > mx:
            mx = v
            w = k

    return (w, mx)



words = sorted(wordFrequency('idiot.mw'))
print(words[0:100])

