# Uses barycentric technique described at http://www.blackpawn.com/texts/pointinpoly/

import csv

def diff(v1, v2):
  return [v1[0] - v2[0], v1[1] - v2[1]]

def dot(v1, v2):
  return v1[0] * v2[0] + v1[1] * v2[1]


def origin_in_triangle(a, b, c):
  p = [0, 0]
  v0 = diff(c, a)
  v1 = diff(b, a)
  v2 = diff(p, a)
  dot00 = dot(v0, v0)
  dot01 = dot(v0, v1)
  dot02 = dot(v0, v2)
  dot11 = dot(v1, v1)
  dot12 = dot(v1, v2)
  inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)
  u = (dot11 * dot02 - dot01 * dot12) * inv_denom
  v = (dot00 * dot12 - dot01 * dot02) * inv_denom
  inside = (u > 0) and (v > 0) and (u + v < 1)
  return inside

def solve():
  count = 0
  line_count = 0
  file = open('problem102_data.txt')
  reader = csv.reader(file)
  for row in reader:
    row = list(map(int, row))
    a = [row[0], row[1]]
    b = [row[2], row[3]]
    c = [row[4], row[5]]
    if origin_in_triangle(a, b, c):
      count += 1
    line_count += 1
  print(count, line_count)
  file.close()

print(origin_in_triangle([-340, 495], [-153, -910], [835, -947]))
print(origin_in_triangle([-175, 41], [-421, -714], [574, -645]))

solve()
