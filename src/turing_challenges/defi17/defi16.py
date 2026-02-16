#!/usr/bin/env python3

import sys
import argparse

from turing_challenges.utils import positive_int

def get_sum_dividers(n) :
  from math import sqrt,ceil
  lDivider = []
  for i in range(1,ceil(sqrt(n))+1) :
    if n%i==0 :
      lDivider.append(i)
      lDivider.append(n/i)
  return int(sum(lDivider)-n)

def get_amical_numbers(nlim) :
  dsomme = {i:get_sum_dividers(i) for i in range(1,nlim+1) if get_sum_dividers(i)<=nlim}
  return [(k,v) for k,v in dsomme.items() if v in dsomme.keys() and dsomme[v]==k and k!=v]

def solve_challenge16(n) :
    return sum([couple[0] for couple in get_amical_numbers(n+1)])

def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the sum of amical numbers between 1 and n."
    )

    parser.add_argument(
        "n",
        type=positive_int,
        help="maximum value",
    )

    ### Extract parameters
    args = parser.parse_args(argv)


    print(solve_challenge16(args.n))

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)