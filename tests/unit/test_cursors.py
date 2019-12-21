from primes.cursor import Cursor, PrimeCursor


def test_get_values():
    c = Cursor(11, 2)
    expected_gen = [13, 15, 17, 19, 21, 23, 25]
    gen = c.values(5)
    assert gen == expected_gen

def test_update():
    c = Cursor(11, 2)
    c.values(5)  
    assert c.current == 25

def test_prime_cursor():
    p3 = PrimeCursor(3)
    assert p3.base == 3
    assert p3.multiplier == 1

def test_prime_cursor_mult():
    p3 = PrimeCursor(3, 4)
    assert p3.base == 3
    assert p3.multiplier == 4

def test_prime_next():
    p3 = PrimeCursor(3, 2)
    n = p3.next()
    # assert n == 9
