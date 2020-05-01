from typing import List, Set
import numpy as np


def floor_sqrt(x: int) -> int:
    """
    Calculates floor(sqrt(x)).
    :param x: a number.
    :return: a integer.
    """
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i) ** 2 <= x:
            y += i
        i //= 2
    return y

def ceil_sqrt(x: int) -> int:
    """
    Calculates ceil(sqrt(x)).
    :param x: a number.
    :return: a integer.
    """
    return floor_sqrt(x) + 1


def is_prime(x: int) -> bool:
    """
    :param x: An integer
    :return: True if x is a prime.
    """
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, ceil_sqrt(x), 2):
        if x % i == 0:
            return False

    return True


def list_primality(n: int) -> np.ndarray:
    """
    result[i] == True if i is a prime number.
    Calculate using Sieve of Eratosthenes algorithm.
    :param n: a positive number.
    :return: a numpy bool array with shape (n + 1,).
    """
    assert n > 0
    result = np.ones([n + 1], dtype=bool)
    result[0:2] = False # 0 and 1
    for i in range(ceil_sqrt(n)):
        if result[i]:
            result[i * i::i] = False

    return result


def list_primes(n: int) -> np.ndarray:
    """
    :param n:
    :return: A numpy array with all prime numbers up to and including to n in ascading order.
    """
    return np.where(list_primality(n))[0]


def factorize(n: int) -> Set[int]:
    factors = set()
    for i in range(1, ceil_sqrt(n)):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)

    return factors


def smallest_prime_factor(n: int) -> int:
    assert n >= 2
    for i in range(2, ceil_sqrt(n)):
        if n % i == 0:
            return i

    return n

