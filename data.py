import random


def rand_bigint(n=10):
    digits = [str(random.randint(1, 9))]
    for _ in range(n - 1):
        digits.append(str(random.randint(0, 9)))

    number_str = ''.join(digits)

    if random.choice([True, False]):
        number_str = "-" + number_str

    return number_str
