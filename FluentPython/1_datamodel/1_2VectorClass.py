from math import hypot


class Vector:


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)


    def __abs__(self):
        return hypot(self.x, self.y) # Return the Euclidean distance, sqrt(x*x + y*y).

vector = Vector(1, 2)
print(len(vector))


print(memoryview(bytes(123)))
print(memoryview(bytes(1)))
print(memoryview(bytes('hello world', encoding='utf-8')))
# print(memoryview(bytes(Vector())))