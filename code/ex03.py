
units = ['', 'մեկ', 'երկու', 'երեք', 'չորս', 'հինգ', 'վեց', 'յոթ', 'ութ', 'ինը']
tens = ['', 'տաս', 'քսան', 'երեսուն', 'քառասուն', 'հիսուն',
        'վաթսուն', 'յոթանասուն', 'ութսուն', 'ինսուն']


def numberToWords(num):
    # միանիշ
    if num < 10:
        return units[num]
    
    # երկնիշ
    if num < 100:
        m = num % 10
        t = num // 10
        return tens[t] + ('ը' if m == 0 and t == 1 else 'ն') + units[m]

    # եռանիշ
    if num < 1000:
       h = num // 100
       m = num % 100
       return units[h] + ' հարյուր ' + numberToWords(m) 

    # քառանիշ, հնգանիշ ու վեցանիշ
    if num < 1000000:
        w = num % 1000
        h = num // 1000
        return numberToWords(h) + ' հազար ' + numberToWords(w)

    return ''



#print(numberToWords(111111))
#print(numberToWords(26439))
#print(numberToWords(3928))
print(numberToWords(10))
print(numberToWords(110))
print(numberToWords(4010))
print(numberToWords(16))
print(numberToWords(118))
print(numberToWords(4011))
