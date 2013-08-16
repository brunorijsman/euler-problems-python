import math

debug = False

best = {}

def solve():
    return solve_max_size(12000)

def solve_max_size(max_size):
    for n in range(2, max_size):
        recurse([n], n, max_size)
    del(best[1])
    if debug:
        show_best(max_size)
    return sum(set(best.values()))

def recurse(factors, product, max_size):
    consider(factors, product, max_size)
    n = factors[-1]
    while n * product <= 2 * max_size:
        recurse(factors + [n], n * product, max_size)
        n += 1

def consider(factors, product, max_size):
    ones = product - sum(factors)
    if ones >= 0:
        size = len(factors) + ones
        if size <= max_size:
            if (size not in best) or (best[size] > product):
                new_best = True
                best[size] = product
            else:
                new_best = False
            if debug:
                show(factors, ones, new_best, size)

def show(factors, ones, new_best, size):
    padded = [1] * ones + factors
    print " * ".join(map(str, padded)), "=",
    print " + ".join(map(str, padded)), "=",
    print sum(padded),
    if new_best:
        print "new best for size", size
    else:
        print "not best for size", size

def show_best(max_size):
    print
    print "*** Lowest product for each size ***"
    for size in range(2, max_size + 1):
        print size, "->", best[size]
    print
    print "*** Unique best products ***"
    print best
    print best.values()
    print set(best.values())
