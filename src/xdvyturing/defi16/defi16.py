#!/usr/bin/env python3

import sys
import argparse
import itertools
from typing import Sequence

def get_letters(cryptarithme) :
  return set(let for let in cryptarithme if let.isalpha())

def get_corresponding_eq(cryptarithme,dtable) :
  calcul = cryptarithme
  for let,val in dtable.items() :
    calcul = calcul.replace(let,str(val))
  calcul = " ".join([str(int(k)) if k.isnumeric() else k for k in calcul.split(" ")])
  return calcul

def get_possible_tables(cryptarithme) :
  import itertools
  lpossibility = []
  l_letters = get_letters(cryptarithme)
  lchiffres = [0,1,2,3,4,5,6,7,8,9]
  if len(l_letters) != len(lchiffres) :
    return NotImplemented
  for p in itertools.permutations(lchiffres):
    dtable = {let:p[i] for i,let in enumerate(l_letters)}
    computation = get_corresponding_eq(cryptarithme=cryptarithme,dtable=dtable)
    if eval(computation) :
      lpossibility.append(dtable)
  return lpossibility

def solve_challenge15(cryptarithme) :
    lpossibility = get_possible_tables(cryptarithme)
    return get_corresponding_eq(cryptarithme=cryptarithme,dtable=lpossibility[0])

def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the product of the maximum and minimum value of the sums of products of each line in a square of 9 values."
    )

    ### Extract parameters
    args = parser.parse_args(argv)

    
    cryptarithme = "THREE * NINE == TROIS * NEUF"
    result = [str(eval(uncrypted)) for uncrypted in solve_challenge15(cryptarithme).split("==")]
    print(" == ".join(result))

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)