#!/usr/bin/env python3

import sys
import argparse
import math

def compute_sum(n: int) -> int:
    '''
    Return the sum of the digits of an integer.
    
    :param n: Integer
    :return: Sum of the digits
    '''
    return sum(int(i) for i in str(n))

def digits_in_factorial(n: int) -> int:
    if n < 2:
        return 1
    return int(sum(math.log10(i) for i in range(1, n + 1))) + 1


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the sum of digits of factorial n : n!."
    )

    parser.add_argument(
        "n",
        type=int,
        help="Integer n",
    )

    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Allow calculation above Python's safe limit (up to 8000). May consume large memory.",
    )


    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display the value of n! (or the number of digits if n> 10**10)",
    )

    ### Extract parameters
    args = parser.parse_args(argv)
    n = args.n

    ABSOLUTE_MAX_DIGITS = 8000

    sys_limit = sys.get_int_max_str_digits()
    digits = digits_in_factorial(n)

    if digits > ABSOLUTE_MAX_DIGITS:
        print(
            "Error: requested computation exceeds hard safety limits.",
            file=sys.stderr
        )
        return 3

    if digits > sys_limit and not args.force:
        print(
            f"Error: {n}! has {digits} digits, exceeding the safe limit ({sys_limit}). Use --force to override.",
            file=sys.stderr
        )
        return 2
    
    if args.force:
        print(f"Warning: computing {n}! may use ~{digits} digits of memory", file=sys.stderr)
        new_limit = digits + 100  # marge de sécurité
        sys.set_int_max_str_digits(new_limit)

    nfact = math.factorial(n)

    if args.verbose: 
        if nfact < 10**10:
            print(nfact)
        else:
            print(f"n! has {digits} digits - too big to display")

    digit_sum = compute_sum(nfact)

    print(digit_sum)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)