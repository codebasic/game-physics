import math
from decimal import Decimal
import numbers

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = Decimal(x)
        self.y = Decimal(y)
        self.z = Decimal(z)

    def _getTypeErrorMsg(operator, other):
        return 'unsupported operand type(s) for {}: {} and {}'.format(
            operator, self.__class__, type(other))

    def __iter__(self):
        for coord in (self.x, self.y, self.z):
            yield coord

    def __repr__(self):
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)

    def __str__(self):
        return '({:.2f}, {:.2f}, {:.2f})'.format(self.x, self.y, self.z)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Vector(x, y, z)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
            return Vector(x, y, z)

        elif isinstance(other, numbers.Number):
            return self.__rmul__(other)

    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return Vector(x, y, z)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return Vector(x, y, z)

    def __floordiv__(self, other):
        x = self.x // other
        y = self.y // other
        z = self.z // other
        return Vector(x, y, z)

    # augmented assignments
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        else:
            self.x -= other
            self.y -= other
            self.z -= other

        return self

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        self.z /= other
        return self

    def __ifloordiv__(self, other):
        self.x //= other
        self.y //= other
        self.z //= other
        return self

    def __pow__(self, other, modulo=None):
        x = self.x ** other
        y = self.y ** other
        z = self.z ** other
        return Vector(x, y, z)

    # unary
    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __abs__(self):
        return Decimal(math.sqrt(self.x**2+self.y**2+self.z**2))

class Body:
    def __init__(self, mass, position):
        self.mass = Decimal(mass)
        self.position = Vector(*position)

    @property
    def weight(self):
        return self.mass * Decimal(9.81)

    @property
    def first_moment(self):
        return self.mass * self.position

    def __repr__(self):
        return 'Body({}, {})'.format(self.mass, str(self.position))
