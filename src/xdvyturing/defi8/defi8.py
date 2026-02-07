#!/usr/bin/env python3

import sys
import argparse
import math
from xdvyturing.utils import positive_int

def count_squares_in_rectangle(n: int, m: int) -> int:
    '''
    Compute the number of square that can be drawn in a rectangle of nxm.
    
    :param n: length of the square/rectangle
    :type n: int
    :param m: width of the square/rectangle
    :type m: int
    '''

    # L'aire est égale au nombre de carrés de 1
    # Pour savoir le nombre de carré de 2 possibles dans un rectangle de nxm : (n-1)*(m-1)
    # Pour calculer le nombre de carré de 3 possibles dans un rectangle de nxm : (n-2)*(m-2)
    # Pour calculer le nombre de carré de l possibles dans un rectangle de nxm : (n+1-l)*(m+1-l)

    if n < 1 or m < 1:
        raise ValueError("n and m must be >= 1")
    
    count = 0
    for i in range(min(n,m)) :
        count += (n-i)*(m-i)
    return count


def rectangles_with_exactly_n_squares(n: int) :
    '''
    Yield all rectangle dimensions (i, j) such that the rectangle contains exactly n squares. 
    
    :param n: number of square that can be drawn in the rectangle
    :type n: int
    :return: generator
    '''

    if n < 1 :
        raise ValueError("n must be >= 1")
    
    max_len = int(math.sqrt(n))+1
    return ((height,width) for height in range(1,max_len) for width in range(height,max_len) if count_squares_in_rectangle(height,width)==n)


def area_closest_square(n: int) :
    '''
    Compute the area of the rectangles containing n squares and return the one with the closest shape of a square. 
    
    :param n: number of square that can be drawn in the rectangle
    :type n: int
    '''

    if n < 1 :
        raise ValueError("n must be >= 1")

    best = None
    for height,width in rectangles_with_exactly_n_squares(n) :
        if best is None or abs(height-width) < abs(best[1]-best[0]) :
            best = (height,width)

    return best


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the area of the rectangle containing n squares with the closest shape to a square."
    )

    parser.add_argument(
        "n",
        type=positive_int,
        help="Number of squares contained in the rectangle",
    )

    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Allow calculation above Python's safe limit (up to 100000). May consume large memory.",
    )

    ### Extract parameters
    args = parser.parse_args(argv)

    # Upper bound on n to prevent excessive CPU usage.
    ABSOLUTE_MAX_N = 100000
    DEFAULT_MAX_N= 50000

    n = args.n
    
    if n > ABSOLUTE_MAX_N :
        print(
            f"Error: requested computation exceeds hard safety limits.",
            file=sys.stderr
        )
        return 3
    
    if n > DEFAULT_MAX_N and not args.force:
        print(
            f"Error: {n} exceeds the safe limit ({DEFAULT_MAX_N}). Use --force to override.",
            file=sys.stderr
        )
        return 2
    
    if args.force:
        print(f"Warning: Large n may lead to long runtimes.", file=sys.stderr)

    (height,width) = area_closest_square(n)
    
    print(height*width)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)