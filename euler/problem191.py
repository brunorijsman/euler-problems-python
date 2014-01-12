prize_count_cache = {}
simple_prize_count_cache = {}

def prize_string_count(length):

  if length in prize_count_cache:
    return prize_count_cache[length]

  if length <= 0:
    return 1

  if length == 1:
    # O, L, A
    return 3    

  if length == 2:
    # OO, OL, OA, LO, LA, AO, AL, AA
    return 8

  count = 0
  count += prize_string_count(length - 1)          # O...
  count += simple_prize_string_count(length - 1)   # L...
  count += prize_string_count(length - 2)          # AO...
  count += simple_prize_string_count(length - 2)   # AL... 
  count += prize_string_count(length - 3)          # AAO...
  count += simple_prize_string_count(length - 3)   # AAL...

  prize_count_cache[length] = count
 
  return count

def simple_prize_string_count(length):

  if length in simple_prize_count_cache:
    return simple_prize_count_cache[length]

  if length <= 0:
    return 1

  if length == 1:
    # O, A
    return 2

  if length == 2:
    # OO, OA, AO, AA
    return 4

  count = 0
  count += simple_prize_string_count(length - 1)   # O...
  count += simple_prize_string_count(length - 2)   # AO...
  count += simple_prize_string_count(length - 3)   # AAO...

  simple_prize_count_cache[length] = count

  return count

print(prize_string_count(30))
