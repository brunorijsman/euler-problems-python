cache = {}

def count(max_more_digits, allow_leading_zero, needed_digits):

  index = (max_more_digits, allow_leading_zero, needed_digits)
  if index in cache:
    return cache[index]

  cnt = 0

  # Is the number we have constructed so far a solution?

  if needed_digits == "":
    cnt += 1
  
  # Try to find more solutions by exending the number.

  if max_more_digits > 0:

    if allow_leading_zero:
      allowed_digits = "0123456789ABCDEF"
    else:
      allowed_digits = "123456789ABCDEF"
      
    for digit in allowed_digits:

      if digit in needed_digits:
        new_needed_digits = needed_digits.replace(digit, "")
      else:
        new_needed_digits = needed_digits

      cnt += count(max_more_digits - 1, True, new_needed_digits)

  # Done

  cache[index] = cnt
  return cnt

def solve():
  print(hex(count(16, False, "01A")).upper())

solve()
