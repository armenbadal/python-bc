
def rectangle(f, x0, x1):
    dx = x1 - x0
    return f(x0) * dx

def trapezoidal(f, x0, x1):
    dx = x1 - x0
    return (f(x0) + f(x1)) / 2 * dx

def integral(f, a, b):
    FRAGMENTS = 1e4
    DELTA = (b - a) / FRAGMENTS

    result = 0.0

    x = a
    while x < b:
        y = f(x) * DELTA
        result += y
        x += DELTA

    return result



#
#
#
v0 = integral(lambda x: x * x, 0, 4)
print(v0)

#
v1 = integral(lambda x: x, 0, 4)
print(v1)
