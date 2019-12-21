
class Node(object):
    """ Container for values in a doubly linked list data structure """

    def __init__(self, value):
        self.value = value
        self._next = None
        self._previous = None

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __hash__():
        return self.value.hash

    def insert_after(self, node):
        self._next = node
        node._previous = self
        return self

    def insert_before(self, node):
        self._previous = node
        node._next = self
        return node

    def __str__(self):
        return str(value)


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
