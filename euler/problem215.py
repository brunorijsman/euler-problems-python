from copy import copy

def count_walls(width, height):
  indents = [0] * height
  return count_walls_with_indent(indents, width)

cache = {}

def count_walls_with_indent(indents, width):

  # Too wide?
  if max(indents) > width:
    return 0

  # Crack?
  for i1 in range(1, len(indents)):
    if indents[i1] not in [0, width]:
      if indents[i1] == indents[i1 - 1]:
        return 0

  # Normalize
  common = min(indents)
  if common > 0:
    indents = list(map(lambda x: x - common, indents))
    width -= common

  # Solution?
  if width == 0:
    return 1

  # --- check cache
  problem = (tuple(indents), width)
  if problem in cache:
    return cache[problem]

  # Determine number of ways to extend current indent to valid walls
  extensions = 0

  # Choose row to extend
  min_index = 0
  for index in range(1, len(indents)):
    if indents[index] < indents[min_index]:
      min_index = index

  # Extend chosen row with 2
  new_indents = copy(indents)
  new_indents[min_index] += 2
  extensions += count_walls_with_indent(new_indents, width)
  
  # Extend chosen row with 3
  new_indents = copy(indents)
  new_indents[min_index] += 3
  extensions += count_walls_with_indent(new_indents, width)

  cache[problem] = extensions
  return extensions

def solve():
  print(count_walls(32, 10))

solve()
