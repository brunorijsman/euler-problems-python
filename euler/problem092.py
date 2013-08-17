import array
import time

def sum_square_digits(nr):
    total = 0
    while nr != 0:
        total += (nr % 10) ** 2
        nr //= 10
    return total

def arrive_at_89(nr):
    while True:
        if nr == 1:
            return False
        if nr == 89:
            return True
        nr = sum_square_digits(nr)

def solve_max(max):
    max_sum = sum_square_digits(max - 1)
    result = array.array('i', [0] * (max_sum + 1))
    for nr in range(1, max_sum + 1):
        result[nr] = arrive_at_89(sum_square_digits(nr))
    count = 0
    for nr in range(1, max):
        next_nr = sum_square_digits(nr)
        if result[next_nr]:
            count += 1
    return count

def solve():
    return solve_max(10000000)

print(solve_max(1000))
