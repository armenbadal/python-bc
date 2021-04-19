
class MyEx(Exception):
    def __str__(self):
        return 'MYEX'

def f():
    raise MyEx

def g():
    open('abcd.txt', 'r')

try:
    f()
except Exception as ex:
    print(ex)
except ValueError as ve:
    print(ve)
finally:
    print('Ok')
