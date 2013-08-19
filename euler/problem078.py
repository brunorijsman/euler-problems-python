""" Euler problem 78 "coin partitions". Solution based on the
    "recurrence equation" described at 
     https://oeis.org/wiki/Partition_function#Partition_function_recurrence """

import math

partitions_known = {}

def partitions(n):
    total = 0
    bound = math.floor((1 + math.sqrt(1 + 24*n)) / 6)
    for j in range(1, bound + 1):
        if j % 2 == 0:
            factor = -1
        else:
            factor = 1
        index = n - j * (3*j - 1) // 2
        total += factor * partitions_known[index]
    bound = math.floor((-1 + math.sqrt(1 + 24*n)) / 6)
    for j in range(1, bound + 1):
        if j % 2 == 0:
            factor = -1
        else:
            factor = 1
        index = n - j * (3*j + 1) // 2
        total += factor * partitions_known[index]
    partitions_known[n] = total
    return total

def solve_divisor(divisor):
    global partitions_known 
    partitions_known = {0: 1}
    n = 1
    while True:
        if partitions(n) % divisor == 0:
            return n
        n += 1

def solve():
    return solve_divisor(1000000)
