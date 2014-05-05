def dominates(l1, l2):
  for (n1, n2) in zip(l1, l2):
    if n1 <= n2:
      return False
  return True
  
def needs_check(x, y):
  if len(x) != len(y):
    return False
  if len(x) <= 1:
    return False
  if dominates(y, x):
    return False
  return True

def visit_all_pairs(s):
  return visit_all_pairs_recurse(s, [], [])

def visit_all_pairs_recurse(s, x, y):
  if s == []:
    if needs_check(x, y):
      return 1
    else:
      return 0
  first = s[0]
  rest = s[1::]
  count = 0
  count += visit_all_pairs_recurse(rest, x + [first], y)
  if x != []:
    count += visit_all_pairs_recurse(rest, x, y + [first])
  count += visit_all_pairs_recurse(rest, x, y) 
  return count

print (visit_all_pairs(range(1,13)))
