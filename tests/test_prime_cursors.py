#! /usr/bin/env python

from primes.cursor import PrimeCursor

def test_imports():
    assert True

def test_three():
    c3 = PrimeCursor(3)
    assert c3.get() == 9

def test_inc():
    c3 = PrimeCursor(3)
    assert(c3.increment() == 15)

