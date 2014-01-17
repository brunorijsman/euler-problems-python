UNKNOWN = 0

def print_grid(grid):
  for r in range(0, 9):
    for c in range(0, 9):
      if grid[r][c] == UNKNOWN:
        print('.', end='')
      else:
        print(grid[r][c], end='')
    print()
  return True
  
def find_open_pos(grid):
  for r in range(0, 9):
    for c in range(0, 9):
      if grid[r][c] == UNKNOWN:
        return (r, c)
  return None

def value_in_row(v, r, grid):
  for c in range(0, 9):
    if grid[r][c] == v:
      return True
  return False

def value_in_column(v, c, grid):
  for r in range(0, 9):
    if grid[r][c] == v:
      return True
  return False

def value_in_block(v, r, c, grid):
  base_r = r - r%3
  base_c = c - c%3
  for r2 in range(base_r, base_r + 3):
    for c2 in range(base_c, base_c + 3):
      if grid[r2][c2] == v:
        return True
  return False

def can_add_value(v, r, c, grid):
  if value_in_row(v, r, grid):
    return False
  if value_in_column(v, c, grid):
    return False
  if value_in_block(v, r, c, grid):
    return False
  return True
  
def solve_grid(grid):
  pos = find_open_pos(grid)
  if pos == None:
    return True
  r = pos[0]
  c = pos[1]
  for v in range(1, 10):
    if can_add_value(v, r, c, grid):
      grid[r][c] = v
      if solve_grid(grid):
        return True
      grid[r][c] = UNKNOWN
  return False

def solve():
  file = open('problem096_data.txt')
  sum = 0
  while True:
    name = file.readline().rstrip('\n')
    if not name:
      break
    grid = []
    for r in range(0, 9):
      row_str = file.readline()
      row = []
      for c in range(0, 9):
        row.append(int(row_str[c]))
      grid.append(row)
    assert(solve_grid(grid) == True)
    top_left = grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
    sum += top_left
  file.close()
  print(sum)

solve()
