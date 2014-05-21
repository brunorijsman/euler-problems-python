import copy

def read_logins(file_name):
  logins = []
  file = open(file_name)
  for login in file:
    login = login.rstrip('\n')
    logins.append(login)
  file.close()
  return logins

def search(passcode, successors):
  if not successors:
    if passcode[-1] == '>':
      return passcode
    else:
      return False
  last_digit = passcode[-1]
  if last_digit not in successors:
    return False
  for next_digit in successors[last_digit]:
    new_passcode = passcode + next_digit
    new_successors = copy.copy(successors)
    del(new_successors[last_digit])
    found = search(new_passcode, new_successors)
    if found:
      return found
  return False

def compute_successors(logins):
  successors = {}
  for login in logins:
    prev = '<'
    for c in login:
      if prev not in successors:
        successors[prev] = set()
      successors[prev].add(c)
      prev = c
    if c not in successors:
      successors[c] = set()
    successors[c].add('>')
  return successors  
  
def solve():
  logins = read_logins('problem79_data.txt')
  successors = compute_successors(logins)
  return(search('<', successors))

print(solve())
