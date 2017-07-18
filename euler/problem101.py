from fractions import Fraction

"""

  We want to determine the optimum polynomial OP(k,n) for a given degree k-1:

  OP(k,n) = a(0) + a(1) * n + a(2) * n^2 + ... + a(k-1) * n^(k-1)

  Plugging values n = 1...k into OP(k, n) must generate the series u(n):

  OP(k, 1) = u(1)
  OP(k, 2) = u(2)
  OP(k, 3) = u(3)
  ...
  OP(k, k) = u(k)

  Expanding OP we get:

  a(0)   +   a(1) * 1   +   a(2) * 1^2   + ... +   a(k-1) * 1^(k-1)   =   u(1)
  a(0)   +   a(1) * 2   +   a(2) * 2^2   + ... +   a(k-1) * 2^(k-1)   =   u(2)
  a(0)   +   a(1) * 3   +   a(2) * 2^2   + ... +   a(k-1) * 2^(k-1)   =   u(2)
  ...
  a(0)   +   a(1) * k   +   a(2) * k^2   + ... +   a(k-1) * k^(k-1)   =   u(k)

  Rewriting this in matrix form, we have to solve the following matrix equation for a:

  M * a = u

  where M, a, and u are as follows:

  [   1   1   1   ...   1         ]   [  a(0)  ]     [ u(1) ]
  [   1   2   4   ...   2^(k-1)   ]   [  a(1)  ]     [ u(2) ]
  [   1   3  27   ...   3^(k-1)   ]   [  a(2)  ]  =  [ u(3) ]
                  ...                    ...
  [   k k^2 k^3   ...   k^(k-1)   ]   [ a(k-1) ]     [ u(k) ]

  Note that indexing is it bit akward because of the choice of indexing in the Euler
  problem: in the above equation we sometimes start with index 0 and sometimes with
  index 1.

  We solve this matrix equation by constructing the following augmented matrix of
  dimensions k * k+1 and then applying Gaussian elimination.

  For exact precision we store all numbers are fractions.

  Once we have OP(k,n) it is trivial to find the FIT for values n.

"""

def u_example(n):
    return n**3

def u_problem(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def make_augmented_matrix(u_function, k):
    matrix = []
    for r in range(0, k):
        row = []
        for c in range(0, k):
            row.append(Fraction((r+1) ** c))
        row.append(Fraction(u_function(r+1)))
        matrix.append(row)
    return matrix

def sweep_row(matrix, target_row_index, adjust_row_index, factor):
    nr_columns = len(matrix[0])
    for c in range(0, nr_columns):
        matrix[target_row_index][c] -= factor * matrix[adjust_row_index][c]

def gaussian_elimination(matrix):
    nr_rows = len(matrix)
    nr_columns = len(matrix[0])
    # Sweep down    
    for ari in range(0, nr_rows):
        for tri in range(ari+1, nr_rows):
            factor = Fraction(matrix[tri][ari], matrix[ari][ari])
            sweep_row(matrix, tri, ari, factor)
    # Sweep up
    for ari in reversed(range(1, nr_rows)):
        for tri in reversed(range(0, ari)):
            factor = Fraction(matrix[tri][ari], matrix[ari][ari])
            sweep_row(matrix, tri, ari, factor)
    # Normalize
    for ri in range(0, nr_rows):
         matrix[ri][nr_rows] /= matrix[ri][ri]
         matrix[ri][ri] = Fraction(1, 1)
    # Return solution
    solution = []
    for ri in range(0, nr_rows):
        solution.append(matrix[ri][nr_columns-1])
    return solution

def compute_optimum_polynomial_coeficients(u_function, k):
    matrix = make_augmented_matrix(u_function, k)
    coeficients = gaussian_elimination(matrix)
    return coeficients

def optimum_polynomial(coeficients, n):
    k = len(coeficients)
    fn = Fraction(n)
    result = Fraction(0)
    for i in range(0, k):
        fi = Fraction(i)
        result += coeficients[i] * (fn ** fi)
    return result

def first_incorrect_term(u_function, k):
    coeficients = compute_optimum_polynomial_coeficients(u_function, k)
    n = k + 1
    while True:
        potentially_incorrect_term = optimum_polynomial(coeficients, n)
        if potentially_incorrect_term != u_function(n):
            return potentially_incorrect_term
        n += 1

def sum_of_first_incorrect_terms(u_function, u_degree):
    sum = 0
    for k in range(1, u_degree+1):
        sum += first_incorrect_term(u_function, k)
    return sum

assert(sum_of_first_incorrect_terms(u_example, 3) == 74)

print(sum_of_first_incorrect_terms(u_problem, 10))
