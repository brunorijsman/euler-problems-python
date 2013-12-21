# Takes more than one minute. Sub-minute solution is too boring.

def reverse(n):
  rev_n = 0
  while n > 0:
    rev_n = 10 * rev_n + n % 10
    n //= 10
  return rev_n

def all_odd(n):
  while n > 0:
    digit = n % 10
    if digit % 2 == 0:
      return False
    n //= 10
  return True

def solve_up_to_limit(limit):
  count = 0
  for n in range(limit):
    if (n % 10 != 0):          # no trailing 0 allowed
      sum = n + reverse(n)
      if all_odd(sum):
        count += 1
  return count
         
def solve():
  print(solve_up_to_limit(1000000000))
