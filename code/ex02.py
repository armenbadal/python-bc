
ms = ['', 'մեկ', 'երկու', 'երեք', 'չորս', 'հինգ', 'վեց', 'յոթ', 'ութ', 'ինը']
ts = ['', 'տաս', 'քսան', 'երեսուն', 'քառասուն', 'հիսուն', 'վաթսուն', 
      'յոթանասուն', 'ութսուն', 'ինսուն']

def numberToWords(n):
    if n < 10:
        return ms[n]

    if n < 100:
        m = n % 10
        t = n // 10
        return ts[t] + ('ը' if t == 1 and m == 0 else 'ն') + ms[m]
    
    if n < 1000:
        t = n % 100
        h = n // 100
        return ms[h] + ' հարյուր ' + numberToWords(t)

    if n < 1000000:
        return numberToWords(n // 1000) + ' հազար ' + numberToWords(n % 1000)

    return ''



print(numberToWords(2))
print(numberToWords(9))

print(numberToWords(10))
print(numberToWords(11))
print(numberToWords(19))
print(numberToWords(47))
print(numberToWords(99))

print(numberToWords(100))
print(numberToWords(101))
print(numberToWords(110))
print(numberToWords(348))

print(numberToWords(1010))
print(numberToWords(3482))
print(numberToWords(34871))
print(numberToWords(341298))

print(numberToWords(999999))
print(numberToWords(101010))
