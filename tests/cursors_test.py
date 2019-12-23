def test_basic():
    assert True

from primes.cursors import PrimeCursor


def test_prime_cursor():
    p3 = PrimeCursor(3)
    assert p3.base == 3
    assert p3.multiplier == 3

def test_prime_cursor_mult():
    p3 = PrimeCursor(3, 5)
    assert p3.base == 3
    assert p3.multiplier == 5

