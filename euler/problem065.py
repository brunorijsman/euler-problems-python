from fractions import Fraction

def fixed():
  return 2

def nth(n):
  if n % 3 == 1:
    return (n // 3 + 1) * 2
  else:
    return 1

def tail(start_term, total_terms):
  if start_term == total_terms:
    return Fraction(1, nth(start_term))
  else:
    a = Fraction(nth(start_term))
    b = tail(start_term + 1, total_terms)
    return 1 / (a + b)

def convergent(terms):
  f = Fraction(fixed())
  if terms > 1:
    t = tail(0, terms - 2)
  else:
    t = 0
  return f + t

def sum_digits(n):
  return sum([int(c) for c in str(n)])

def solve():
  print(sum_digits(convergent(100).numerator))
  
solve()
