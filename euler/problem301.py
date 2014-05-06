import time

def is_lost(x, y, z):
  return (x ^ y ^ z) == 0

def solve():
  count = 0
  for n in xrange(1, 2 ** 30 + 1):
    if is_lost(n, 2*n, 3*n):
      count += 1
  print count

def timed_solve():
  time1 = time.time()
  solve()
  time2 = time.time()
  print 'time =', time2 - time1

timed_solve()
