""" Project Euler problem 220: Heighway Dragon """

# A journey is a tuple (forward, lateral, turn, steps) where
#   forward is number of steps in the facing direction (negative is backwards)
#   lateral is number of steps to the right relative to facing direction (negative is left)
#   turn is change of facing orientiation: 0=no turn, 1=right 90, 2=right 180, 3=right 270=left 90
#   steps taken in the journey

nop = (0, 0, 0, 0)
forward = (1, 0, 0, 1)
right = (0, 0, 1, 0)
left = (0, 0, 3, 0)

fwd = 0
lat = 1
trn = 2
stp = 3

cache = {}

def dragon(n, steps):
    journey = forward
    (stage, truncated) = ab_stage('a', n, steps-1)
    journey = append(journey, stage)
    return journey

def ab_stage(ab, n, max_steps):

    # Bottom of recursion
    if n == 0:
        return (nop, False)

    # Use cache, if available, unless it overshoots the desired number of steps
    key = (ab, n)
    if key in cache:
        stage = cache[key]
        if stage[stp] <= max_steps:
            return (stage, False)

    # The recursion rules for a Heighway Dragon
    if ab == 'a':
        pattern = "aRbFR"
    else:
        pattern = "LFaLb"

    stage = nop
    for c in pattern:

        # How much remaining steps before we reach the max number of steps?
        remaining_max_steps = max_steps - stage[stp]
        assert remaining_max_steps >= 0

        # If we have reached the max, truncate and return the stage thus far
        if remaining_max_steps == 0:
            return (stage, True)

        # Compute the next stage corresponding to the letter in the pattern,
        # making sure not to overshoot the remaining number of steps.
        if (c == 'a') or (c == 'b'):
            (next_stage, truncated) = ab_stage(c, n-1, remaining_max_steps)
        elif c == 'L':
            next_stage = left
            truncated = False
        elif c == 'R':
            next_stage = right
            truncated = False
        elif c == 'F':
            next_stage = forward
            truncated = False

        # Append the next stage to the running total.
        stage = append(stage, next_stage)

        # Bail out once we have reached the desired number of steps.
        if truncated:
            return (stage, True)

    # We finished a potentially expensive computation of an a(n) or b(n) stage
    # without truncation. Cache and return the result.
    cache[key] = stage
    return (stage, False)

def append(journey, stage):
    return add(journey, align(stage, journey[trn]))

def align(stage, direction):
    """ Rotate the next stage of the journey to align with the direction in
        which the end of the journey thus far points. """
    if direction == 0:
        return stage
    elif direction == 1:
        return (-stage[1], stage[0], stage[2], stage[3])
    elif direction == 2:
        return (-stage[0], -stage[1], stage[2], stage[3])
    elif direction == 3:
        return (stage[1], -stage[0], stage[2], stage[3])

def add(j1, j2):
    return (j1[fwd] + j2[fwd],
            j1[lat] + j2[lat],
            (j1[trn] + j2[trn]) % 4,
            j1[stp] + j2[stp])

def solve(n, steps):
    # The starting position was on the origin, facing towards the positive side of the y-axis
    (y, x, direction, actual_steps) = dragon(n, steps)
    return (x,y)

print(solve(50, 1000000000000))
