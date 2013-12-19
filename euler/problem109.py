triple_regions = list(range(1, 21))
double_regions = triple_regions + [25]
single_regions = double_regions

def add_solution(solutions, checkout, befores, score):
  normalized_befores = sorted(befores)
  solution = tuple(normalized_befores + [checkout])
  solutions.add(solution)

def find_befores(checkout, befores, score, solutions, max_score):
  if (len(befores) == 2):
    return
  for region in single_regions:
    throw_score = region
    if score + throw_score <= max_score:
      throw = 'S' + str(region)
      new_score = score + throw_score
      new_befores = befores + [throw]
      add_solution(solutions, checkout, new_befores, new_score)
      find_befores(checkout, new_befores, new_score, solutions, max_score)
  for region in double_regions:
    throw_score = 2 * region
    if score + throw_score <= max_score:
      throw = 'D' + str(region)
      new_score = score + throw_score
      new_befores = befores + [throw]
      add_solution(solutions, checkout, new_befores, new_score)
      find_befores(checkout, new_befores, new_score, solutions, max_score)
  for region in triple_regions:
    throw_score = 3 * region
    if score + throw_score <= max_score:
      throw = 'T' + str(region)
      new_score = score + throw_score
      new_befores = befores + [throw]
      add_solution(solutions, checkout, new_befores, new_score)
      find_befores(checkout, new_befores, new_score, solutions, max_score)

def find_checkouts(solutions, max_score):
  for region in double_regions:
    throw_score = 2 * region
    if throw_score <= max_score:
      throw = 'D' + str(region)
      add_solution(solutions, throw, [], throw_score)
      find_befores(throw, [], throw_score, solutions, max_score)

def solve_for_max_score(max_score):
  solutions = set()
  find_checkouts(solutions, max_score)
  print(len(solutions))

def solve():
  solve_for_max_score(99)

solve()
