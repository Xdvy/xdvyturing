#!/usr/bin/env python3

import sys
import argparse
import itertools
from typing import Sequence

def blue_value(p: Sequence[int]) -> int:
    '''
    Compute the sum of products of each line in a square of 9 values
    '''

    if len(p) != 9 :
        raise ValueError("Exactly 9 integers required.")
    
    return (
        p[0]*p[1]*p[2]
        + p[3]*p[4]*p[5]
        + p[6]*p[7]*p[8]
        + p[0]*p[3]*p[6]
        + p[1]*p[4]*p[7]
        + p[2]*p[5]*p[8]
    )


def min_max_blue_product(values=None):
    '''
    Compute the product of the maximum and minimum value of the sums of products of each line in a square of 9 values.
    '''

    if values is None:
        values = [1,2,3,4,5,6,7,8,9]

    if len(values) != 9:
        raise ValueError("Exactly 9 values required.")

    min_blue = None
    max_blue = None

    for p in itertools.permutations(values):
        current = blue_value(p)
        if min_blue is None or current < min_blue:
            min_blue = current
        if max_blue is None or current > max_blue:
            max_blue = current

    return min_blue * max_blue


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the product of the maximum and minimum value of the sums of products of each line in a square of 9 values."
    )

    parser.add_argument(
        "--values",
        nargs=9,
        type=int,
        default=[1,2,3,4,5,6,7,8,9],
    )


    ### Extract parameters
    args = parser.parse_args(argv)

    try :
        print(min_max_blue_product(values=args.values))
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)