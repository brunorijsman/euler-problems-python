# Euler problem 091: "Right triangles with integer coordinates"

def solve(grid_size):

    # Brute-force try all possible locations for P and Q
    count = 0
    for px in range(grid_size+1):
        for py in range(grid_size+1):
            for qx in range(grid_size+1):
                for qy in range(grid_size+1):
                    if is_right_triangle(px, py, qx, qy):
                        count += 1

    # Because of P-Q symmetry, everything was counted twice
    return count // 2

def is_right_triangle(px, py, qx, qy):

    # If the triangle is right-angled, it must obey the Pythagorean theorem

    # Distance Origin to P (squared)
    dops = px ** 2 + py ** 2

    # Distance Origin to Q (squared)
    doqs = qx ** 2 + qy ** 2

    # Distance P to Q (squared)
    dpqs = (qx - px) ** 2 + (qy - py) ** 2

    # None of the distances are allowed to be zero
    if (dops == 0) or (doqs == 0) or (dpqs == 0):
        return False

    # Right angle at 0?
    if dops + doqs == dpqs:
        return True

    # Right angle at P?
    if dops + dpqs == doqs:
        return True

    # Right angle at Q?
    if doqs + dpqs == dops:
        return True
 
    # No right angle
    return False

print(solve(50))
