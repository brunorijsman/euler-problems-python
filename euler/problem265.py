def recurse(n, ring, remaining, pos):
    if pos == (2**n) - 2:
        add_ring(n, ring)
    else:
        candidate = (ring[pos] & (2**(n-1) - 1)) << 1
        consider(n, ring, remaining, pos, candidate)
        consider(n, ring, remaining, pos, candidate+1)

def consider(n, ring, remaining, pos, candidate):
    if candidate in remaining:
        ring[pos+1] = candidate
        remaining.remove(candidate)
        recurse(n, ring, remaining, pos+1)
        del ring[pos+1]
        remaining.append(candidate)

def add_ring(n, ring):
    global sum
    representation = 0
    for i in range(0, 2**n):
        representation *= 2
        if ring[i] & 2**(n-1):
            representation += 1
    sum += representation

def solve(n):
    global sum
    sum = 0
    ring = {}
    ring[0] = 0
    ring[1] = 1
    remaining = list(range(2, 2**n))
    ring[2**n - 1] = 2**(n-1)
    remaining.remove(2**(n-1))
    recurse(n, ring, remaining, 1)
    print sum

solve(5)
