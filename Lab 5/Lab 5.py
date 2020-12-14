import math
class Fraction:
    """Находим сумму сложения двух дробей"""
    def __init__(self, n, d):
        self.num = int(n / self.gcd(abs(n), abs(d)))
        self.denom = int(d / self.gcd(abs(n), abs(d)))
        if self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1 * self.num
        elif self.denom == 0:
            raise ZeroDivisionError
 
    def gcd(self, n, d):
        while n != d:
            if n > d:
                n = n - d
            else:
                d = d - n
        return n
    
    def __Add__(self, other):
        return self.num * other.denom + self.denom * other.num, self.denom * other.denom
    def __str__(self):
        if type(self) is tuple:
            if self[1] < 0:
                return '%s/%s' % (self[0], -1 * self[1])
            else:
                return '%s/%s' % (self[0], self[1])

    def __le__(self, other):
        return math.sqrt(self.num ** 2 + other.denom ** 2 + self.denom ** 2 + other.num ** 2) <= math.sqrt(self.denom ** 2 + other.num ** 2 + self.num ** 2 + other.denom ** 2)
    def __li__(self, other):
        return math.sqrt(self.num ** 2 + other.denom ** 2 + self.denom ** 2 + other.num ** 2) < math.sqrt(self.denom ** 2 + other.num ** 2 + self.num ** 2 + other.denom ** 2)
    def __la__(self, other):
        return math.sqrt(self.num ** 2 + other.denom ** 2 + self.denom ** 2 + other.num ** 2) >= math.sqrt(self.denom ** 2 + other.num ** 2 + self.num ** 2 + other.denom ** 2)
    def __lo__(self, other):
        return math.sqrt(self.num ** 2 + other.denom ** 2 + self.denom ** 2 + other.num ** 2) > math.sqrt(self.denom ** 2 + other.num ** 2 + self.num ** 2 + other.denom ** 2)
f1 = Fraction(3,-3)
f2 = Fraction(3,-3)
f3 = Fraction.__Add__(f1,f2)
print(Fraction.__str__(f3))
print(Fraction.__Add__(f1,f2))
print(Fraction.__le__(f1,f2))
print(Fraction.__li__(f1,f2))
print(Fraction.__la__(f1,f2))
print(Fraction.__lo__(f1,f2))
