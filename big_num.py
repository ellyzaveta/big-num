from typing import Union


class BigNum:
    BASE = 1000000000

    def __init__(self, value: Union[int, str] = 0):
        if isinstance(value, int):
            self._from_int(value)
        elif isinstance(value, str):
            self._from_str(value)
        else:
            raise ValueError("Invalid initialization value")

    def _from_int(self, value):
        self.is_negative = value < 0
        self.digits = []
        value = abs(value)
        while value > 0:
            self.digits.append(value % BigNum.BASE)
            value //= BigNum.BASE

    def _from_str(self, value: str):
        if not value:
            self.is_negative = False
            self.digits = [0]
            return
        if value[0] == "-":
            self.is_negative = True
            value = value[1:]
        else:
            self.is_negative = False
        self.digits = []
        value = value.lstrip('0') or '0'
        for i in range(len(value), 0, -9):
            if i < 9:
                self.digits.append(int(value[:i]))
            else:
                self.digits.append(int(value[i - 9:i]))

    def __str__(self):
        if not self.digits:
            return "0"
        result = []
        if self.is_negative:
            result.append("-")
        result.append(str(self.digits[-1]))
        for digit in self.digits[-2::-1]:
            result.append(str(digit).rjust(9, '0'))
        return ''.join(result)

    def __neg__(self):
        result = BigNum(str(self))
        result.is_negative = not self.is_negative
        return result

    def __lt__(self, other):
        if self.is_negative and not other.is_negative:
            return True
        if not self.is_negative and other.is_negative:
            return False

        if self.is_negative and other.is_negative:

            if len(self.digits) < len(other.digits):
                return False
            if len(self.digits) > len(other.digits):
                return True
            for i in range(len(self.digits) - 1, -1, -1):
                if self.digits[i] > other.digits[i]:
                    return True
                elif self.digits[i] < other.digits[i]:
                    return False
        else:
            if len(self.digits) < len(other.digits):
                return True
            if len(self.digits) > len(other.digits):
                return False
            for i in range(len(self.digits) - 1, -1, -1):
                if self.digits[i] < other.digits[i]:
                    return True
                elif self.digits[i] > other.digits[i]:
                    return False
        return False

    def __eq__(self, other):
        return self.is_negative == other.is_negative and self.digits == other.digits

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self < other) and not (self == other)

    def __ge__(self, other):
        return not (self < other)

    def odd(self):
        return self.digits[0] % 2 != 0

    def even(self):
        return not self.odd()

    def _remove_leading_zeros(self):
        while len(self.digits) > 1 and self.digits[-1] == 0:
            self.digits.pop()

    def __add__(self, other):
        if isinstance(other, int):
            other = BigNum(other)
        if self.is_negative != other.is_negative:
            if self.is_negative:
                return other - (-self)
            else:
                return self - (-other)

        result = BigNum()
        carry = 0
        max_len = max(len(self.digits), len(other.digits))
        for i in range(max_len):
            x = self.digits[i] if i < len(self.digits) else 0
            y = other.digits[i] if i < len(other.digits) else 0
            temp_sum = x + y + carry
            carry = temp_sum // BigNum.BASE
            result.digits.append(temp_sum % BigNum.BASE)
        if carry:
            result.digits.append(carry)

        result.is_negative = self.is_negative
        return result

    def __sub__(self, other):
        if isinstance(other, int):
            other = BigNum(other)

        if self.is_negative != other.is_negative:
            if self.is_negative:
                return -((-self) + other)
            else:
                return self + (-other)

        if not self.is_negative and self < other:
            return -(other - self)

        if self.is_negative and self > other:
            return (-other) - (-self)

        result = BigNum()
        carry = 0

        for i in range(len(self.digits)):
            x = self.digits[i]
            y = other.digits[i] if i < len(other.digits) else 0
            temp_diff = x - y - carry

            if temp_diff < 0:
                temp_diff += BigNum.BASE
                carry = 1
            else:
                carry = 0

            result.digits.append(temp_diff)

        result._remove_leading_zeros()
        result.is_negative = self.is_negative
        return result

    def __mul__(self, other):
        if isinstance(other, int):
            other = BigNum(other)
        result = BigNum()
        result.digits = [0] * (len(self.digits) + len(other.digits))

        for i in range(len(self.digits)):
            carry = 0
            for j in range(len(other.digits) + 1):
                if j == len(other.digits) and carry == 0:
                    break
                y = other.digits[j] if j < len(other.digits) else 0
                cur = result.digits[i + j] + self.digits[i] * y + carry
                result.digits[i + j] = cur % BigNum.BASE
                carry = cur // BigNum.BASE

        result.is_negative = self.is_negative != other.is_negative
        result._remove_leading_zeros()
        return result

    def __pow__(self, exponent):
        if exponent == 2:
            return self * self
        else:
            raise ValueError("Only squaring is currently supported.")

    def __lshift__(self, shift):
        if isinstance(shift, int) and shift >= 0:
            result = BigNum(str(self))
            for _ in range(shift):
                result.digits.insert(0, 0)
            return result

    def __rshift__(self, shift):
        if isinstance(shift, int) and shift >= 0:
            result = BigNum(str(self))
            for _ in range(shift):
                if result.digits:
                    result.digits.pop(0)
            return result

    def __divmod__(self, other):
        if isinstance(other, int):
            other = BigNum(other)

        if other == BigNum(0):
            raise ZeroDivisionError("Division by zero")

        dividend = BigNum(str(self))
        divisor = BigNum(str(other))
        dividend.is_negative = False
        divisor.is_negative = False

        if dividend < divisor:
            return BigNum(0), self

        quotient = BigNum()
        current = BigNum()
        for i in range(len(dividend.digits) - 1, -1, -1):
            current = (current << 1) + BigNum(dividend.digits[i])
            q_digit = 0
            while current >= divisor:
                current -= divisor
                q_digit += 1
            quotient.digits.insert(0, q_digit)

        quotient._remove_leading_zeros()
        quotient.is_negative = self.is_negative != other.is_negative
        current.is_negative = self.is_negative

        return quotient, current

    def __truediv__(self, other):
        quotient, _ = self.__divmod__(other)
        return quotient

    def __mod__(self, other):
        _, remainder = self.__divmod__(other)
        return remainder

    def __floordiv__(self, other):
        return self.__truediv__(other)



