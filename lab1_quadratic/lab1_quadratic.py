# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function

def discriminant(b, c):
    return b**2 - 4*c


def root_to_str(x):
    return '{:+.10f}{:+.10f}j'.format(x[0], x[1])


def solve_quadratic(b, c):
    D = discriminant(b, c)
    if D >= 0:
        x1 = ((-b + D**0.5) / 2, 0.0)
        x2 = ((-b - D**0.5) / 2, 0.0)
    else:
        x1 = (-b / 2, (-D)**0.5 / 2)
        x2 = (-b / 2, -(-D)**0.5 / 2)
    return root_to_str(x1)+' '+root_to_str(x2)


if __name__ == "__main__":
    b = float(input())
    c = float(input())
    roots = solve_quadratic(b, c)
    print(roots)
