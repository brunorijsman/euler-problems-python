"""
We know the optimum set for n = 6 is {11, 18, 19, 20, 22, 25}.

Using the rule, we know that {20, 31, 38, 39, 40, 42, 45} is a special
sum set, but possibly not the optimum set.

That gives an upper bound for S(A) for n = 7 of 20 + 31 + ... + 45 =
255

Knowing an upper bound allows us to do an exhaustive search.

Implementing the exhaustive search makes use of the following observation:
if {a1, a2, ..., an-1, an} is a special sum set, then {a1, a2, ..., an-1}
is also a special sum set.
"""

import time

n = 7
upper_bound = 255

def check_properties(x, y):
  if len(x) > len(y):
    return sum(x) > sum(y)
  elif len(x) < len(y):
    return sum(x) < sum(y)
  else:
    return sum(x) != sum(y)

def is_special_sum_set(s):
  return check_all_disjoint_subsets(s, [], [])

def check_all_disjoint_subsets(s, x, y):
  if s == []:
    if x != [] and y != []:
      return check_properties(x, y)
    else:
      return True
  first = s[0]
  rest = s[1::]
  return (check_all_disjoint_subsets(rest, x + [first], y) and
          check_all_disjoint_subsets(rest, x, y + [first]) and
          check_all_disjoint_subsets(rest, x, y))

def recurse(solution):
  if not is_special_sum_set(solution):
    return
  if len(solution) == n:
    print('solution =', solution)
    return True
  if solution == []:
    start = 19
  else:
    start = solution[-1]
  leeway = upper_bound - sum(solution)
  more_digits = n - len(solution)
  end = leeway // more_digits
  for i in range(start + 1, end + 1):
    if recurse(solution + [i]):
      return True
  return False

def solve():
  time1 = time.time()
  recurse([])
  time2 = time.time()
  print('time =', time2 - time1)

solve()
