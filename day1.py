#!/usr/bin/env python3

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.

# Print the sum of the double variables on a new line.

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.




if __name__ == '__main__':
    no_of_lines = 3
    lines = ""
    for n in range(1, no_of_lines+1):
        if n == 1:
            x = int(input().strip())
            print(x + i)
        elif n == 2:
            x = float(input().strip())
            print(x + d)
        elif n == 3:
            x = str(input().strip())
            print(s + x)
        
