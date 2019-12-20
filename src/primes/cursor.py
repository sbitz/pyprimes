
class Cursor(object):
    def __init__(self, start, increment):
        self.current = start
        self.increment = increment

    def values(self, base):
        result = list(range(self.next(), base**2+1, self.increment))
        self.current = result[-1]
        return result

    def next(self):
        return self.current + self.increment


class PrimeCursor(object):
    def __init__(self, prime, mult=1):
        self.base = prime
        self.multiplier = mult



