import math

def root_period(n):
  i = int(math.sqrt(n))
  if i * i == n:
    return 0
  digit_list = []
  iterate(n, 1, i, digit_list, [])
  return(len(digit_list))

def iterate(n, a, b, digit_list, ab_list):
  k = int(float(a) / (math.sqrt(n) - float(b)))
  new_a = (n - b*b) // a
  new_b = -1 * (b - k * new_a)
  if not (a,b) in ab_list:
    digit_list.append(k)
    ab_list.append((a,b))  
    iterate(n, new_a, new_b, digit_list, ab_list)

def solve():
  count = 0
  for n in range(2, 10001):
    if root_period(n) % 2 == 1:
      count += 1
  print(count)

solve()
