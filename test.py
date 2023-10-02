import unittest
from _decimal import getcontext
from decimal import Decimal
from data import rand_bigint
from big_num import BigNum
import random


class TestBigNum(unittest.TestCase):
    getcontext().prec = 100

    def test_addition(self):
        a = rand_bigint(random.randint(30, 50))
        b = rand_bigint(random.randint(30, 50))
        big_num1 = BigNum(a)
        decimal1 = Decimal(a)
        big_num2 = BigNum(b)
        decimal2 = Decimal(b)

        self.assertEqual(str(big_num1 + big_num2), str(decimal1 + decimal2))

    def test_subtraction(self):
        a = rand_bigint(random.randint(30, 50))
        b = rand_bigint(random.randint(30, 50))

        big_num1 = BigNum(a)
        decimal1 = Decimal(a)
        big_num2 = BigNum(b)
        decimal2 = Decimal(b)

        self.assertEqual(str(big_num1 - big_num2), str(decimal1 - decimal2))

    def test_multiplication(self):
        a = rand_bigint(random.randint(30, 50))
        b = rand_bigint(random.randint(30, 50))
        big_num1 = BigNum(a)
        decimal1 = Decimal(a)
        big_num2 = BigNum(b)
        decimal2 = Decimal(b)

        self.assertEqual(str(big_num1 * big_num2), str(decimal1 * decimal2))

    def test_mod(self):
        a = rand_bigint(random.randint(30, 35))
        b = rand_bigint(random.randint(30, 35))

        big_num1 = BigNum(a)
        decimal1 = Decimal(a)
        big_num2 = BigNum(b)
        decimal2 = Decimal(b)

        self.assertEqual(str(big_num1 % big_num2), str(decimal1 % decimal2))

    def test_comparison(self):
        a = rand_bigint(random.randint(30, 50))
        b = rand_bigint(random.randint(30, 50))
        big_num1 = BigNum(a)
        decimal1 = Decimal(a)
        big_num2 = BigNum(b)
        decimal2 = Decimal(b)

        self.assertEqual(big_num1 < big_num2, decimal1 < decimal2)
        self.assertEqual(big_num1 <= big_num2, decimal1 <= decimal2)
        self.assertEqual(big_num1 > big_num2, decimal1 > decimal2)
        self.assertEqual(big_num1 >= big_num2, decimal1 >= decimal2)
        self.assertEqual(big_num1 == big_num2, decimal1 == decimal2)
        self.assertEqual(big_num1 != big_num2, decimal1 != decimal2)

    def test_square(self):
        a = rand_bigint(random.randint(30, 50))

        big_num1 = BigNum(a)
        decimal1 = Decimal(a)

        self.assertEqual(str(big_num1 ** 2), str(decimal1 ** 2))


if __name__ == "__main__":
    unittest.main()
