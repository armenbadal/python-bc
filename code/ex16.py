
def islatin(c):
    return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

def read(name):
    letters = {}

    with open(name, 'r') as fin:
        for line in fin:
            for c in [e.lower() for e in line if islatin(e)]:
                letters[c] = letters.get(c, 0) + 1
    
    kv = list(letters.items())
    kv.sort(key=lambda e: e[1], reverse=True)
    return kv


def codes(n):
    if n == 1:
        return [['.', '-']]

    cs = codes(n - 1)
    csa = ['.' + c for c in cs[-1]]
    csb = ['-' + c for c in cs[-1]]
    cs.append(csa + csb)
    return cs


#print(codes(3))
print(read('martin-eden.txt'))
