from fractions import *

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(size):
    bn = 2
    bd = 5
    bf = float(bn)/float(bd)

    for d in range(size, 0, -1):
        if d % 100 == 0: print d, bn, bd
        for n in range(d*3/7, 0, -1):
            f = float(n)/float(d)
            if f < bf:
                break
            if gcd(n, d) == 1 and (n, d) != (3, 7):
                bn, bd, bf = n, d, f
                break
    print best

solve(1000000)