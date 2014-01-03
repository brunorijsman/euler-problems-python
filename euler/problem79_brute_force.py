# Brute force; works but takes too long

def read_logins(file_name):
  logins = []
  file = open(file_name)
  for login in file:
    login = login.rstrip('\n')
    logins.append(login)
  file.close()
  return logins

def is_consistent(passcode, login):
  last_index = -1
  for c in login:
    index = passcode.find(c, last_index + 1)
    if index <= last_index:
      return False
    last_index = index
  return True

def is_conistent_with_all(passcode, logins):
  for login in logins:
    if not is_consistent(passcode, login):
      return False
  return True

def solve():
  logins = read_logins('problem79_data.txt')
  passcode = 100
  while not is_conistent_with_all(str(passcode), logins):
    passcode += 1
  return passcode

print(solve())
