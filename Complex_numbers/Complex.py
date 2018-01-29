from __future__ import division
from math import sqrt
from math import atan, degrees


class Complex(object):

    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img

    def __repr__(self):
        if self.img < 0:
            return "%s%si" % (self.real, self.img)
        elif self.img > 0:
            return "%s+%si" % (self.real, self.img)
        else:
            return "%s" % (self.real)

    def __add__(self, other):
        real = self.real + other.real
        img = self.img + other.img
        return Complex(real, img)

    def __sub__(self, other):
        real = self.real - other.real
        img = self.img - other.img
        return Complex(real, img)

    def __mul__(self, other):
        real = (self.real * other.real) - (self.img * other.img)
        img = (self.real * other.img) + (self.img * other.real)
        return Complex(real, img)

    def conjugate(self):
        return Complex(self.real, -self.img)

    def abs(self):
        return sqrt(self.real**2 + self.img**2)

    def __pow__(self, num):
        for _ in range(num):
            self = self * self
        return self

    def __truediv__(self, other):
        num = self.__mul__(other.conjugate())
        den = (other.abs())**2
        return Complex(num.real/den, num.img/den)

    def angle(self):
        angle_in_radian = atan(self.real/self.img)
        angle_in_degrees = degrees(angle_in_radian)
        if self.real > 0 and self.img > 0:
            return angle_in_degrees
        elif self.real < 0 and self.img > 0:
            return angle_in_degrees + 90
        elif self.real < 0 and self.img < 0:
            return angle_in_degrees + 180
        else:
            return angle_in_degrees + 270

    def polarform(self):
        return "%s(cos(%s) + sin(%s)i)" % (self.abs(), self.angle(), self.angle())

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __ne__(self, other):
        return not self == other





