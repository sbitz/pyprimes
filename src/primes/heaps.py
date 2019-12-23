from .cursors import PrimeCursor


class FibNode(object):
    def __init__(self, k, v):
        self.key = k
        self.container = [v]
        self.children = []
        self.marked = False
        self.degree = 0

    def __len__(self):
        _len = len(self.container)
        for x in self.children:
            _len += x.len
        return _len

    def __repr__(self):
        return "%s" % self.key

    def __str__(self):
        return self.key

    def add_child(self, other):
        self.children.append(other)
        self.degree = max(self.degree, other.degree + 1)

    @staticmethod
    def merge(node1, node2):
        node1.container += node2.container
        node1.children += node2.children
        node1.marked = node1.marked or node2.marked
        node1.degree = max(node1.degree, node2.degree)
        return node1


class FibHeap(object):

    def __init__(self):
        self.roots = []

    def __len__(self):
        _len = 0
        for r in self.roots:
            _len += len(r)
        return _len

    def link(self):
        """ link roots into deeper trees and make roots[0] the smallest value """
        refs = {}
        self.roots.reverse()

        for root in self.roots:
            degree = root.degree
            # see if we need to merge trees
            if not refs.has_key(degree):
                refs[degree] = root
            else:
                current = root
                while refs.has_key(degree):
                    other = refs.pop(degree)

                    if other.key < current.key:
                        other.add_child(current)
                        new_root = other
                    elif other.key == current.key:
                        new_root = FibNode.merge(current, other)
                    else:
                        current.add_child(other)
                        new_root = current

                    # new_root now contains joined root node
                    current = new_root
                    degree = current.degree

                # end join with refs loop
                refs[degree] = current

        self.roots = refs.values()
        self.roots.sort()

    def delete_min(self):
        # remove current min
        root_node = self.roots.pop(0)
        # add children as new roots
        self.roots += root_node.children
        # relink and find new min root
        self.link()

        if len(self.roots) > 1:
            assert self.roots[-1] > self.roots[0]

        return root_node

    def update_key(self, n):

        while self.get_min_key() == n:
            # remove root node in the normal delete fashion
            min_node = self.delete_min()
            for cursor in min_node.container:
                cursor.increment()
                self.add_cursor(cursor)

    def get_min_key(self):
        if self.roots is None:
            raise Exception('empty heap')
        return self.roots[0].key

    def add_cursor(self, cursor):
        node = FibNode(cursor.get(), cursor)

        if not self.roots or node.key < self.get_min_key():
            self.roots.insert(0, node)
        else:
            self.roots.append(node)

    def add_prime(self, value):
        cursor = PrimeCursor(value)
        self.add_cursor(cursor)

    def test(self, n):
        min_key = self.get_min_key()
        if n < min_key:
            self.add_prime(n)
            return True
        elif n == min_key:
            self.update_key(n)
            return False
        else:
            print(n)
            raise Exception('not yet implemented')  # check the state for this condition


def up_to(maximum):
    prime_list = [3]
    h = FibHeap()
    len(h)
    h.add_prime(3)

    print('min key should be 9: %s' % h.get_min_key())
    for n in range(5, maximum, 2):
        if h.test(n):
            prime_list.append(n)

    print(prime_list)
    return prime_list


if __name__ == '__main__':
    up_to(200)
