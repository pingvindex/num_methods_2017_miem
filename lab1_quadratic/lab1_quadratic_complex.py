# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function

def discriminant(b, c):
    return b**2 - 4*c


def solve_quadratic(b, c):
    D = discriminant(b, c)
    if D >= 0:
        if b >= 0:
            x2 = (-b - D**0.5) / 2
            x1 = c / x2
        else:
            x1 = (-b + D**0.5) / 2
            x2 = c / x1
    else:
        x1 = complex((-b) / 2, (-D)**0.5 / 2)
        x2 = complex((-b) / 2, -(-D)**0.5 / 2)
    return str(x1).strip('(').strip(')')+' '+str(x2).strip('(').strip(')')


if __name__ == "__main__":
    b = float(input())
    c = float(input())
    roots = solve_quadratic(b, c)
    print(roots)
