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


def solve():
  total = 0
  file = open('problem105_data.txt', 'r')
  for line in file:
    strings = line.rstrip('\n').split(',')
    numbers = [int(str) for str in strings]
    if is_special_sum_set(numbers):
      total += sum(numbers)
  file.close()
  print(total)

solve()
