#!/bin/python3

import math
import os
import random
import re
import sys

# Reverse an array and print as a string
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print(' '.join(map(str, arr[::-1])))
