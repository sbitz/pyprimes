#! /usr/bin/env python



class Queue(object):

    def __init__(self):
        self.list = None
        self.head = None


class Node(object):
    def __init__(self, value):
        self.value = value
        self._previous = None
        self._next = None
    
    def __iter__(self):
        pass

    def __next__(self):
        pass

    def insert_before(self, node):
        print('inserting %s before %s' % (node, self))
        self._previous = node
        node._next = self
        print('done insert: %s -> %s' % (node, self))

    def insert_after(self, node):
        self._next = node
        node._previous = self

    def __repr__(self):
        return "<Node value:%s _previous:%s _next:%s>" % (self.value, self._previous, self._next)

    def __str__(self):
        return str(self.value)

    

class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        pass

    def __iter__(self):
        forwards=True
        if forwards:
            self.curr = self.tail
        else:
            self.curr = self.head

        self.iter_dir = forwards
        return self

    def __next__(self):
        node = self.curr
        forwards = self.iter_dir

        if node is not None:
            if forwards:
                self.curr = node.get_next()
            else:
                self.curr = node.get_prev()
            return node
        else:
            raise StopIteration

    def is_empty(self):
        return self.head is None

    def insert(self, value):
        """ 
        Inserts value into the head of the list 
        """
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            # Create the new node
            node = Node(value)

            # register the node with the current head
            self.head.insert_before(node)

            # point the list to the new head
            self.head = node


    def add(self, value):
        """
        Adds value to the end of the list
        """
        if self.is_empty():
            self.create(value)

        # Create the new node
        node = Node(value)

        # Register the node with the current tail
        self.tail.insert_after(node)

        # Point the list to the new tail
        self.tail = node

    

class PrimeFibHeap(object):

    def __init__(self):
        self.root_nodes = Queue()
        self.buffer = Queue()

    def pretty_print(self):
        pass




