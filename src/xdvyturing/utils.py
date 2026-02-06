#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import sys
import argparse
import math

def largest_prime_divisor(n, collect=False):
    """
    Return the largest prime divisor of n.

    If collect=True, also return the list of prime factors.
    """
    if n < 2:
        raise ValueError("n must be >= 2")
    
    factors = [] if collect else None
    current = n
    last = None

    # Factor 2 separately
    while current % 2 == 0:
        last = 2
        if factors is not None:
            factors.append(2)
        current //= 2

    # Odd factors
    i = 3
    while i * i <= current:
        while current % i == 0:
            last = i
            if factors is not None:
                factors.append(i)
            current //= i
        i += 2

    # Remaining prime
    if current > 1:
        last = current
        if factors is not None:
            factors.append(current)

    return factors, last

def is_prime(n: int) -> bool:
    '''
    Check if n is a prime number
    
    :param n: number to test
    :return : True or False
    '''
    if n < 2 :
        return False
    for j in range(3,int(math.sqrt(n))+1,2) :
        if n%j == 0 :
            return False
    return True

def positive_int(value: str) -> int:
    ivalue = int(value)
    if ivalue < 1:
        raise argparse.ArgumentTypeError("n must be a positive integer")
    return ivalue