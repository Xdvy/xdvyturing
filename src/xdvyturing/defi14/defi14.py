#!/usr/bin/env python3

import sys
import argparse
import math
from typing import Iterator, Tuple

from xdvyturing.utils import positive_int

def generate_syracuse(n: int) -> Iterator[int] :
    '''
    Generate syracuse suite with n as the starter
    '''
    while n != 1 :
        n = int(n/2) if n%2==0 else int(3*n+1)
        yield n


def longest_syracuse(n: int) -> int :
    '''
    Return the first integer below n with the longest syracuse suite.
    '''
    i_longest = None
    max_length = 0

    for k in range(1,n) :
        k_length = sum(1 for _ in generate_syracuse(k))
        if k_length > max_length :
            max_length = k_length
            i_longest = k

    return i_longest
            


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the value of the integer below n that has the longest syracuse suite."
    )

    parser.add_argument(
        "n",
        type=positive_int,
        help="maximum value to test",
    )

    ### Extract parameters
    args = parser.parse_args(argv)
    n = args.n

    print(longest_syracuse(n))

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)