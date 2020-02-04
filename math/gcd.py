import math
import sys

def gcd(a, b):
    if a > b:
        # swap them
        c = a
        a = b
        b = c

    divisors_a = []
    for i in range(1, int(a/2)+1):
        if a % i == 0:
            divisors_a.append(i)

    for x in divisors_a[::-1]:
        if b % x == 0:
            return x

print("Greatest common denominator is:", gcd(int(sys.argv[1]), int(sys.argv[2])))

