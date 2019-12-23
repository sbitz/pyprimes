#! /usr/bin/env python

from primes.heaps import FibHeap


def test_imports():
    assert True


def test_start():
    f = FibHeap()
    f.add_prime(3)
    assert f.get_min_key() == 9

def up_to_25():
    prime_list = primes.heaps.up_to(25)
    assert prime_list == [3, 5, 7, 11, 13, 17, 19, 23]

