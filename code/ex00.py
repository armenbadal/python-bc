from functools import reduce


def primeFactors(n):
    items = []

    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
            items.append(factor)
        factor += 1
    
    if n > 1:
        items.append(n)

    return items


if __name__ == '__main__':
    muls = [2, 2, 2, 3, 3, 5, 7, 7, 7, 7, 11, 11, 13, 13, 13, 13]
    k = reduce(lambda x, y: x * y, muls)
    print(k)
    print(primeFactors(k))
