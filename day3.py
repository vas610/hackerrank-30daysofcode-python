#!/bin/python3

import math
import os
import random
import re
import sys

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird


def print_weird(N):
    N_even = N % 2
    if N_even != 0:
        print("Weird")
    elif N_even == 0 and N in range(2, 6):
        print("Not Weird")
    elif N_even == 0 and N in range(6, 21):
        print("Weird")
    elif N_even == 0 and N > 20:
        print("Not Weird")
    else:
        None    
        
            
if __name__ == '__main__':
    N = int(input().strip())
    print_weird(N)
