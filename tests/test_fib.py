

from primes.fib_heap import FibHeap, Heap
from primes.cursor import PrimeCursor

def test_fib_create():
    f = FibHeap()
    l = len(f)
    assert l == 1

def test_heap_create():
    h = Heap()
    assert h.min_value() == None

def test_heap_add():
    h = Heap(3)
    assert h.min_value() == 3

def test_heap_cursor():
    h = Heap(PrimeCursor(3))
    print(h.min_value())
    assert h.min_value().get() == 9

def test_fib_heap_init():
    fh = FibHeap()
    assert len(fh) == 1
    assert fh.get_min() == 9



