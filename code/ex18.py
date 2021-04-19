
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, ovec):
        return Vector(self.x + ovec.x, self.y + ovec.y)

    def __iadd__(self, ovec):
        self.x += ovec.x
        self.y += ovec.y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)



v0 = Vector(1, 2)
v1 = Vector(3, 4)

print(v0)
print(v1)

v3 = v0 + v1
print(v3)
