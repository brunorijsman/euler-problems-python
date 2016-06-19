from itertools import *
from fractions import Fraction

def solve():
    best_highest_target = 0
    for number in combinations(range(0, 10), 4):
        ht = highest_target(number)
        if ht > best_highest_target:
            best_highest_target = ht
            best_number = number
    print best_number

def highest_target(digits):
    frac_digits = tuple([Fraction(d) for d in digits])
    operations = ['+', '-', '*', '/']
    targets = []
    for fds in permutations(frac_digits):
        for ops in product(operations, operations, operations):
            target = eval_target_a(fds, ops)
            if target:
                targets.append(target)
            target = eval_target_b(fds, ops)
            if target:
                targets.append(target)
    highest = 0
    while True:
        if highest + 1 in targets:
            highest += 1
        else:
            break
    return highest

def eval_target_a(frac_digits, operations):
    f1 = eval(frac_digits[0], operations[0], frac_digits[1])
    if not f1:
        return None
    f2 = eval(f1, operations[1], frac_digits[2])
    if not f2:
        return None
    f3 = eval(f2, operations[2], frac_digits[3])
    return f3

def eval_target_b(frac_digits, operations):
    f1 = eval(frac_digits[0], operations[0], frac_digits[1])
    if not f1:
        return None
    f2 = eval(frac_digits[2], operations[2], frac_digits[3])
    if not f2:
        return None
    f3 = eval(f1, operations[1], f2)
    return f3

def eval(f1, op, f2):
    if op == '+':
        return f1 + f2
    elif op == '-':
        return f1 - f2
    elif op == '*':
        return f1 * f2
    elif op == '/':
        if f2 == 0:
            return None
        else:
            return f1 / f2

solve()
