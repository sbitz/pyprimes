
class FibHeap(object):
    
    def __init__(self):
        self._roots = []

    def __len__(self):
        if not self._roots:
            return 0
        count = 0
        for x in self.roots:
            count += len(x)

