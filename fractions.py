from datetime import datetime


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.whole = 0

    @staticmethod
    def change_denominator(n1, dn1, n2,
                           dn2):  # Приведение дробей к общему знаменателю
        numer1 = n1 * dn2
        numer2 = n2 * dn1
        dnumer1 = dn1 * dn2
        dnumer2 = dnumer1
        return numer1, dnumer1, numer2, dnumer2

    @staticmethod
    def reduce_fraction(numerator, denumerator):
        n = dn = 0
        for i in range(2, min(numerator.numerator, denumerator)):
            if denumerator % i == 0 and numerator.numerator % i == 0:
                n = numerator.numerator // i
                dn = denumerator // i
        return n, dn

    def __str__(self):  # Вывод дроби на экран
        self.numerator, self.denominator = Fraction.reduce_fraction(
            abs(self.numerator), abs(self.denominator))
        if self.numerator > self.denominator:
            if self.numerator % self.denominator == 0:
                return str(self.numerator // self.denominator)
            else:
                self.whole = self.numerator // self.denominator
                self.numerator = self.numerator % self.denominator
                return "{0} {1}/{2}".format(self.whole, self.numerator,
                                            self.denominator)
        elif self.numerator == self.denominator:
            return "1"
        else:
            return "{0}/{1}".format(self.numerator, self.denominator)

    def __mul__(self, other):  # Произведение дробей
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __truediv__(self, other):  # Деление дробей
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator)

    def __add__(self, other):  # Сумма дробей
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            self.numerator, self.denominator, other.numerator, other.denominator = Fraction.change_denominator(
                self.numerator, self.denominator, other.numerator,
                other.denominator)
            return Fraction(self.numerator + other.numerator, self.denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        else:
            self.numerator, self.denominator, other.numerator, other.denominator = Fraction.change_denominator(
                self.numerator, self.denominator, other.numerator,
                other.denominator)
            print(self.numerator, self.denominator)
            print(other.numerator, other.denominator)
            print()
            return Fraction(self.numerator - other.numerator, self.denominator)