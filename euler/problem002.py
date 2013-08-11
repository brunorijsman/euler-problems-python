def solve():
    total = 0
    fib = 2
    prev_fib = 1
    while fib <= 4000000:
        if fib % 2 == 0:
            total += fib
        new_fib = fib + prev_fib
        prev_fib = fib
        fib = new_fib
    return total
