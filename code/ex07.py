
def claculateFromFile(name):
    with open(name, 'r') as inp, open('r_'+name, 'w') as out:
        for ex in inp:
            l, op, r = ex.split(' ')
            l = int(l)
            r = int(r)
            
            w = 0
            if op == '+':
                w = l + r
            elif op == '-':
                w = l - r
            elif op == '*':
                w = l * r
            elif op == '//':
                w = l // r
            elif op == '%':
                w = l % r

            out.write(l, op, r, '=', w, '\n')








claculateFromFile('c0.txt')
