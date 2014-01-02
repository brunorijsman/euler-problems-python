known_counts = {}

def last_two(lst):
  return lst[len(lst)-2], lst[len(lst)-1] 

def count_solutions(lst, more_digits, first):
  if more_digits == 0:
    return 1
  prev_prev, prev = last_two(lst)
  problem = (prev_prev, prev, more_digits)
  count = known_counts.get(problem)
  if count != None:
    return count
  prev_sum = prev_prev + prev
  count = 0
  if first:
    start = 1
  else:
    start = 0
  for digit in range(start, 10 - prev_sum):
    count += count_solutions(lst + [digit], more_digits - 1, False)
  known_counts[problem] = count
  return count

def solve():
  return count_solutions([0, 0], 20, True)

print(solve())
