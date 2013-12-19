def count_block(cache, rem_len, block_len):
  if rem_len in cache:
    return cache[rem_len]
  if rem_len >= block_len:
    count = count_block(cache, rem_len - block_len, block_len)
    count += count_block(cache, rem_len - 1, block_len)
  elif rem_len >= 1:
    count = count_block(cache, rem_len - 1, block_len)
  else:
    count = 1
  cache[rem_len] = count
  return count
  
def solve_for_len(len):
  count = count_block(dict(), len, 2) - 1
  count += count_block(dict(), len, 3) - 1
  count += count_block(dict(), len, 4) - 1
  return count

def solve():
  count = solve_for_len(50)
  print(count)

solve()
