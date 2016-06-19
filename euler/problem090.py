# Euler problem 90: Cube digit pairs

def solve():
    
    # Find all possible dies with 6 digits on faces out of 10 combinations
    options = []
    find_options(options, [])
    count = 0

    # Figure out which combinations of two dies make a square
    for die1 in options:
        for die2 in options:
            if is_solution(die1, die2):
                count += 1

    # Devide by 2 because dices can be interchanges (symmetry)
    print(count // 2)
    
def find_options(options, die):
    if len(die) == 6:
        options.append(die)
        return
    if len(die) == 0:
        start = 0
    else:
        start = die[-1] + 1
    for d in range(start, 10):
        find_options(options, die + [d])

def is_solution(die1, die2):
    if not digits_match(die1, die2, 0, 1):
        return False
    if not digits_match(die1, die2, 0, 4):
        return False
    if not digits_match(die1, die2, 0, 9) and not digits_match(die1, die2, 0, 6):
        return False
    if not digits_match(die1, die2, 1, 6) and not digits_match(die1, die2, 1, 9):
        return False
    if not digits_match(die1, die2, 2, 5):
        return False
    if not digits_match(die1, die2, 3, 6) and not digits_match(die1, die2, 3, 9):
        return False
    if not digits_match(die1, die2, 4, 9) and not digits_match(die1, die2, 4, 6):
        return False
    if not digits_match(die1, die2, 6, 4) and not digits_match(die1, die2, 9, 4):
        return False
    if not digits_match(die1, die2, 8, 1):
        return False
    return True

def digits_match(die1, die2, digit1, digit2):
    if (digit1 in die1) and (digit2 in die2):
        return True
    if (digit2 in die1) and (digit1 in die2):
        return True
    return False    

solve()







    
