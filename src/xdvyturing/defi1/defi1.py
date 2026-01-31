#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import sys
import argparse

def multiples(max_value):
    return (i for i in range(max_value) if i % 5 == 0 or i % 7 == 0)

def compute(max_value, verbose=False):
    gen = multiples(max_value)
    if verbose:
        values = list(gen)
        return values, sum(values)
    return None, sum(gen)

def main(argv=None):
    """Main function"""

    parser = argparse.ArgumentParser(
        description="Return the sum of multiples of 5 and 7 less than given value."
    )

    parser.add_argument(
        dest="maxValue",
        type=int,
        help="Maximum value of integers to sum",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbosity",
        default=0,
        action="count",
        help="display list of integers",
    )

    args = parser.parse_args(argv)

    values, total = compute(args.maxValue, args.verbosity)
    if values: print(values)
    print(total)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)

