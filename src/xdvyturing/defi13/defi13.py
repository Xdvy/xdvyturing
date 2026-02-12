#!/usr/bin/env python3

import sys
import argparse
import math
from typing import Iterator, Tuple

from xdvyturing.utils import positive_int

def is_square_palindrome(n: int) -> bool :
    '''
    Check if n^2 is a palindrome, with an even number of digits.
    
    :param n: Description
    '''

    nstring = str(pow(n,2))
    if len(nstring)%2 == 0 and nstring == nstring[::-1]:
        return True
    else :
        return False
    
def searching_next_square_palindrome(n: int) -> Iterator[int] :
    '''
    Docstring pour searching_next_square_palindrome
    
    :param n: Description
    :type n: int
    :return: Description
    :rtype: int
    '''

    n += 1
    searching = True

    while not is_square_palindrome(n) :
        n += 1
    
    return n
            


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the next square palindrome after n."
    )

    parser.add_argument(
        "n",
        type=positive_int,
        help="actual square palindrome",
    )

    ### Extract parameters
    args = parser.parse_args(argv)
    n = args.n

    print(searching_next_square_palindrome(n))

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)