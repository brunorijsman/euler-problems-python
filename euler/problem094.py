# Project Euler 94: Almost equilateral triangles with integral sides and area

# Uses method described at http://www.had2know.com/academics/nearly-equilateral-heronian-triangles.html

limit = 1000000000

def iteration_n_n_np1():
    n1 = 5
    n2 = 65
    n3 = 901
    sum = 3*n1 + 3*n2 + 3*n3 + 3
    while True:
        n1, n2, n3 = n2, n3, 15*n3 - 15*n2 + n1
        perimeter = 3*n3 + 1
        if perimeter > limit:
            return sum
        else:
            sum += perimeter

def iteration_n_np1_np1():
    n1 = 16
    n2 = 240
    n3 = 3360
    sum = 3*n1 + 3*n2 + 3*n3 + 6
    while True:
        n1, n2, n3 = n2, n3, 15*n3 - 15*n2 + n1
        perimeter = 3*n3 + 2
        if perimeter > limit:
            return sum
        else:
            sum += perimeter

print(iteration_n_n_np1() + iteration_n_np1_np1())



    
