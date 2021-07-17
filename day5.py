#!/bin/python3

import math
import os
import random
import re
import sys
import functools


def print_multiples(a, n):
    print(f"{n} x {a} = {n * a}")

a=list(range(1, 11))

if __name__ == '__main__':
    n = int(input().strip())
    x = list(map(functools.partial(print_multiples, n=n), a))
