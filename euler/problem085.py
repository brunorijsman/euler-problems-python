import math

def solve_target(target):
    best_val = -1
    best_diff = target
    best_x = -1
    best_y = -1
    max = math.ceil(math.sqrt(target))
    for x in range(1, max+1):
        for y in range(1, max+1):
            val = (x * (x + 1) // 2) * (y * (y + 1) // 2)
            diff = abs(target - val)
            if diff < best_diff:
                best_x = x
                best_y = y
                best_val = val
                best_diff = diff
    return best_x * best_y

def solve():
    return solve_target(2000000)
