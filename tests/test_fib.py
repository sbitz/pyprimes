
from primes.heaps import FibHeap


def test_fib_create():
    f = FibHeap()
    l = len(f)
    assert l == 0


def test_fib_heap_init():
    fh = FibHeap()
    fh.add_prime(3)
    assert len(fh) == 1
    assert fh.get_min_key() == 9



