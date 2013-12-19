import math
import itertools
from tkinter import *

canvas_width = 800
canvas_height = 800
ring_radius = 100
point_radius = 20

def point_location(point, nr_points):
  arm = point // 2
  nr_arms = nr_points // 2
  mid_x = canvas_width // 2
  mid_y = canvas_height // 2
  base_angle = -math.pi / 2
  one_arm_angle = 2 * math.pi / nr_arms 
  angle = base_angle + arm * one_arm_angle
  inner_x = mid_x + math.cos(angle) * ring_radius
  inner_y = mid_y + math.sin(angle) * ring_radius
  if point % 2 == 0:
    next_x = mid_x + math.cos(angle + one_arm_angle) * ring_radius
    next_y = mid_y + math.sin(angle + one_arm_angle) * ring_radius
    dx = next_x - inner_x
    dy = next_y - inner_y
    x = inner_x - dx
    y = inner_y - dy
  else:
    x = inner_x
    y = inner_y
  return (x, y)
  
def draw_solution(solution):
  nr_points = len(solution)
  nr_arms = nr_points // 2
  tk = Tk()
  canvas = Canvas(tk, width=canvas_width, height=canvas_height)
  canvas.pack()
  for arm in range(nr_arms):
    i1 = (arm*2) % nr_points
    i3 = (arm*2 + 3) % nr_points
    (x1, y1) = point_location(i1, nr_points)
    (x2, y2) = point_location(i3, nr_points)
    canvas.create_line(x1, y1, x2, y2, fill="blue")
  for point in range(nr_points):
    (x, y) = point_location(point, nr_points) 
    canvas.create_oval(x - point_radius, y - point_radius,
                       x + point_radius, y + point_radius,
                       outline="blue",
                       fill="lightblue")
    nr = solution[point]
    canvas.create_text(x, y, text=str(nr))
  canvas.pack()

def same_sums(candidate):
  nr_points = len(candidate)
  nr_arms = nr_points // 2
  sums = []
  for arm in range(nr_arms):
    i1 = (arm*2) % nr_points
    i2 = (arm*2 + 1) % nr_points
    i3 = (arm*2 + 3) % nr_points
    sums.append(candidate[i1] + candidate[i2] + candidate[i3])
  for arm in range(nr_arms - 1):
    if sums[arm] != sums[arm+1]:
      return False
  return True

def first_arm_lowest(candidate):
  nr_points = len(candidate)
  nr_arms = nr_points // 2
  for arm in range(1, nr_arms):
    i = (arm*2) % nr_points
    if candidate[i] < candidate[0]:
      return False
  return True
  
def to_nr(candidate):
  nr_points = len(candidate)
  nr_arms = nr_points // 2
  nr_str = ""
  for arm in range(nr_arms):
    i1 = (arm*2) % nr_points
    i2 = (arm*2 + 1) % nr_points
    i3 = (arm*2 + 3) % nr_points
    nr_str += str(candidate[i1])
    nr_str += str(candidate[i2])
    nr_str += str(candidate[i3])
  return int(nr_str)

def find_best_solution(nr_points, digits):
  max_nr = 0
  best_solution = None
  numbers = list(range(1, nr_points+1))
  for candidate in itertools.permutations(numbers):
    candidate = list(candidate)
    if first_arm_lowest(candidate) and same_sums(candidate):
      nr = to_nr(candidate)
      if (nr > max_nr) and (len(str(nr)) == digits):
        max_nr = nr
        best_solution = candidate
  return best_solution

def solve():
  solution = find_best_solution(10, 16)
  draw_solution(solution)
  print(to_nr(solution))
  
