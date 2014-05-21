# Find the most frequent number in number list 'coded', looking
# only at each 3rd number in the list, starting at offset 'index'

def most_frequent(coded, index):
  counts = {}
  i = index
  while i < len(coded):
    nr = coded[i]
    if nr in counts:
      counts[nr] += 1
    else:
      counts[nr] = 1
    i += 3
  rev = [(freq, cod) for (cod, freq) in counts.items()]
  (max_freq, max_freq_cod) = max(rev)
  return max_freq_cod

# Decode the number list 'coded' using 'key' producing a string

def decode(coded, key):
  decoded = ''
  index = 0
  for nr in coded:
    decoded += chr(nr ^ key[index])
    index = (index + 1) % len(key)
  return decoded  

def solve():

  # Read the coded list of numbers
  
  with open('problem059_data.txt', 'r') as file:
    line = file.read()
  coded = [int(str) for str in line.rstrip('\n').split(',')]
  print(coded)

  # Guess the key, knowing that the characteristics of the key
  # and guessing that the most frequent character is a space
  
  key = []
  for index in [0, 1, 2]:
    most_cod = most_frequent(coded, index)
    key.append(most_cod ^ ord(' '))

  # Print the decoded string
  
  decoded = decode(coded, key)
  print(decoded)

  # Print the sum of the ascii values of the decoded string

  print(sum([ord(x) for x in decoded]))

solve()
