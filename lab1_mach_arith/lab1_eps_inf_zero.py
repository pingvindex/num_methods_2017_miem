# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function

def epsilon():
    N = 0
    while True:
        if 1 + 2.0**(-N) == 1:
            return 2**(-N+1)
        else:
            N+=1


def zero():
    N = 0
    while True:
        if 2.0**(-N) == 0:
            return 2**(-N+1)
        else:
            N+=1


def infty():
    N = 0
    while True:
        try:
            tmp = 2.0**N
        except OverflowError:
            return 2.0**(N-1)
        N += 1


if __name__ == "__main__":
    print(epsilon())
    print(zero())
    print(infty())
