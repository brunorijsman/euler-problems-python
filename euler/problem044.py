def pent(n):
  return n*(3*n-1)//2

def bounded_solve(max_try):
  min_diff = None
  pentagonals = set(pent(n) for n in range(1, max_try))
  for pent1 in pentagonals:
    for pent2 in pentagonals:
      if (pent1 + pent2) in pentagonals and (pent2 - pent1) in pentagonals:
        diff = pent2 - pent1
        if min_diff == None or diff < min_diff:
          min_diff = diff
  print(min_diff)

def solve():
  bounded_solve(2500)

solve()
