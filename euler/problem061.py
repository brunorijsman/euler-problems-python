from numbers import *

def four_digits(fun):
  result = []
  n = 1
  while True:
    value = fun(n)
    digits = number_digits(value)
    if digits == 4:
      result.append(value)
    elif digits > 4:
      return result
    n += 1

def first_two_digits(n):
  # Assumes n is four digits
  return n // 100

def last_two_digits(n):
  # Assumes n is four digits
  return n % 100

def final_checks(cycle, nums):
  # Last two digits of last number equal first two digits of first number
  if (last_two_digits(cycle[-1]) != first_two_digits(cycle[0])):
    return False
  # No number occurs more than once
  for num in cycle:
    if cycle.count(num) > 1:
      return False
  # Each figurate is represented by a different number in the cycle
  for num1 in cycle:
    for num2 in cycle:
      if num1 != num2:
        if nums[num1] == nums[num2]:
          return False
  # For normalization: the first number must be the smallest
  for num in cycle[1:]:
    if num < cycle[0]:
      return False
  return True

def iterate(cycle, needed_len, nums):
  index = len(cycle)
  if index == needed_len:
    if final_checks(cycle, nums):
      return cycle
    return None
  elif index == 0:
    prev = -1
  else:
    prev = cycle[-1]
  for num in nums:
    if (prev == -1) or (last_two_digits(prev) == first_two_digits(num)):
      new_cycle = cycle + [num]
      solution = iterate(new_cycle, needed_len, nums)
      if solution:
        return solution
      
def solve():
  figurates = [(3, triangle),
               (4, square),
               (5, pentagonal),
               (6, hexagonal),
               (7, heptagonal),
               (8, octagonal)]
  nums = {}
  for dim, figurate in figurates:
    for num in four_digits(figurate):
      if num in nums:
        nums[num].append(dim)
      else:
        nums[num] = [dim]
  solution = iterate([], 6, nums)
  print(solution)
  print(sum(solution))

solve()
