

from primes.fib_heap import FibHeap

def test_fib_create():
    f = FibHeap()
    assert len(f) == 0
