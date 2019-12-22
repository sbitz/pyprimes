
class PrimeCursor(object):

    def __init__(self, prime, mult=3):
        self.base = prime
        self.multiplier = mult

    def get(self):
        return self.base * self.multiplier 

    def increment(self):
        self.multiplier += 2
        return self.get()

    def __lt__(self, other):
        s_val = self.get()
        o_val = other.get()
        return s_val < o.val

    def __eq__(self, other):
        s_val = self.get()
        o_val = other.get()
        return s_val == o.val

    def __hash__(self):
        return hash(self.get())

    def __str__(self):
        return "( %s | %s, %s )" % (self.get(), self.base, self.multiplier)

