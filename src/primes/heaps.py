from primes.cursor import PrimeCursor


class Heap(object):
    def __init__(self, value=None):
        if value is not None:
            self._values = [value]
        else:
            self._values = []

    def __len__(self):
        return len(self._values)

    def min_value(self):
        if not self._values:
            return None
        return self._values[0]


class FibHeap(object):
    
    def __init__(self, roots=None):
        if roots is not None:
            self._roots = roots
        else:
            self._roots = [Heap(PrimeCursor(3))]

        self._min_node = None
        self._buffer = []

    def __len__(self):
        if not self._roots:
            return 0
        count = 0
        for x in self._roots:
            count += len(x)
        return count

    def _add_cursor(self, n):
        self._roots.append(Heap(n))

    def get_min(self):
        if self._roots:
            h = self._roots[0]
            value = h.min_value().get()

            if self._buffer:
                return min(value, self._buffer[0])
            else:
                return value
        else:  # No Roots
            if self._buffer:
                return self._buffer[0]
            else:
                return None
    
    def merge(self, other):
        if other.get_min()  < self.get_min():
            return  other._roots + self._roots
        else:
            return self._roots + other._roots

    def test(self, n):
        if n < self.get_min():
            # is prime
            self._add_cursor(n)

    def __str__(self):
        buf_str = "Buffer: %s" % self._buffer
        


    
