def peel_last_digit(n):
    last_digit = n % 10
    rest = n / 10
    return (last_digit, rest)

def direction(n1, n2):
    if n1 > n2:
        return -1
    elif n1 < n2:
        return 1
    else:
        return 0

def is_bouncy(n):
    if n < 10:
        return False
    (prev_last_digit, n) = peel_last_digit(n)
    number_direction = 0
    while n > 0:
        (last_digit, n) = peel_last_digit(n)
        digit_direction = direction(prev_last_digit, last_digit)
        if digit_direction == 0:
            pass
        elif number_direction == 0:
            number_direction = digit_direction
        elif number_direction != digit_direction:
            return True
        prev_last_digit = last_digit
    return False

def solve(target_percent):
    n = 0
    bouncy = 0
    percent = 0.0
    while percent < target_percent:
        n += 1
        if is_bouncy(n):
            bouncy += 1
        percent = 100.0 * bouncy / n
    return n

print solve(99)