from primes.cursor import  PrimeCursor


def test_prime_cursor_mult():
    p3 = PrimeCursor(3, 4)
    assert p3.base == 3
    assert p3.multiplier == 4

def test_prime_next():
    p3 = PrimeCursor(3)
    n = p3.increment()
    assert n == 15
