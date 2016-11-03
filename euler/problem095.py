def solve():
    divisors = {}
    total = {}
    for n in range(1, 1000000):
        divisors[n] = {1, n}
        for d in range(2, n):
            if n % d == 0:
                divisors[n] |= {d} | divisors[n // d]
                break
        total[n] = sum(divisors[n] - {n})
        print(n, divisors[n], total[n])  
            

solve()
