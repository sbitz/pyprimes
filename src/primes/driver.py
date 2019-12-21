#! /usr/env python
from cursor import Cursor, PrimeCursor


def mark_prime(value):
    # print('prime: ' + str(value))
    pass

def mark_composite(value, tc=None):
    if tc is not None:
        tc.increment()
        # print('factor: ' + str(tc.base))


def main(primes=[2, 3, 5, 7]):
    c = Cursor(11, 2)

    prime_filters = [PrimeCursor(n) for n in primes[1:]]
    
    for value in c.values(primes[-1]):
        is_prime = True
        # print('value: ' + str(value))
        for test_cursor in prime_filters:
            while test_cursor.next() < value:
                test_cursor.increment()
            # print('  test: ' + str(test_cursor.next()))
            next_value = test_cursor.next()
            if next_value == value:
                mark_composite(value, test_cursor)
                is_prime = False
            elif next_value < value:
                test_cursor.increment()

        if is_prime:
            mark_prime(value)
            primes.append(value)
            print(value)
        else:
            pass
            # print('composite')
        # print('')
    
    print(" ".join(str(x) for x in primes))
    for cursor in prime_filters:
        print('Cursor('+ str(cursor.base) + ', ' + str(cursor.next()) +')')

if __name__ == '__main__':
    import sys
    args = [int(n) for n in sys.argv[1:]]

    print('args: ' + str(args))
    
    main(args)
