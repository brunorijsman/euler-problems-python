def fac(n):
    fac = 1
    while n > 1:
        fac *= n
        n -= 1
    return fac

facs = {}
for n in range(0, 10):
    facs[n] = fac(n)

def fac_sum(n):
    sum = 0
    while n != 0:
        sum += facs[n % 10]
        n //= 10
    return sum

def non_repeat_len(n):
    seq = []
    while n not in seq:
        seq += [n]
        n = fac_sum(n)
    return len(seq)
    
def solve_max(max):
    count = 0
    for n in range(1, max):
        if non_repeat_len(n) == 60:
            count += 1
    return count

def solve():
    return solve_max(1000000)

