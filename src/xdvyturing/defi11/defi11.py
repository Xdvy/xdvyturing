#!/usr/bin/env python3

import sys
import argparse
from typing import Optional

from xdvyturing.utils import positive_int

def mirror_int(n: int) -> int:
    '''
    Get the exact mirror of integer n (1234:4321)
    '''

    if n < 0:
        raise ValueError("n must be >= 0")
    
    return int(str(n)[::-1])


def largest_mirror_quadruple(n: int) -> Optional[int]:
    '''
    Give the biggest integer k below or equal to n with mirror(k)=4*k
    '''

    biggest = None

    d = len(str(n))
    max_value = int(2.5 * 10**(d-1))

    upper = min(n, max_value)
    for i in range(upper + 1):
        if i%10 != 0 and mirror_int(i) == 4*i :
            biggest = i

    return biggest



def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the biggest integer k below or equal to n with mirror(k)=4*k"
    )

    parser.add_argument(
        "n",
        type=positive_int,
        help="Upper bound to k",
    )

    ### Extract parameters
    args = parser.parse_args(argv)

    n = args.n

    result = largest_mirror_quadruple(n)

    if result is not None:
        print(result)
    else:
        print(f"No value found in the range [0:{n}]")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)