def read_matrix(filename):
  file = open(filename, 'r')
  row = 0
  edges = {}
  for line in file:
    weights = line.rstrip('\n').split(',')
    col = 0
    for weight in weights:
      if weight != '-':
        edges[(row, col)] = int(weight)
      col += 1
    row += 1
  file.close()
  matrix = {'size': row, 'edges': edges}
  return matrix

def cost(matrix):
  return sum(matrix['edges'].values()) // 2

def cost_to_add_vertex_to_tree(tree_vertices, new_vertex, matrix):
  best_attachment_vertex = None
  best_cost = 'infinity'
  for tree_vertex in tree_vertices:
    cost = matrix['edges'].get((new_vertex, tree_vertex))
    if cost != None:
      if best_cost == 'infinity' or cost < best_cost:
        best_attachment_vertex = tree_vertex
        best_cost = cost
  return best_attachment_vertex, best_cost

def minimum_spanning_tree(matrix):
  size = matrix['size']
  tree = {'size': size, 'edges': {}}
  tree_vertices = [0]
  remaining_vertices = list(range(1, size))
  while remaining_vertices:
    best_cost = 'infinity'
    best_vertex = None
    best_attachment_vertex = None
    for vertex in remaining_vertices:
      attachment_vertex, cost = cost_to_add_vertex_to_tree(tree_vertices, vertex, matrix)
      if cost != 'infinity':
        if best_cost == 'infinity' or cost < best_cost:
          best_cost = cost
          best_vertex = vertex
          best_attachment_vertex = attachment_vertex
    tree_vertices.append(best_vertex)
    tree['edges'][(best_vertex, best_attachment_vertex)] = best_cost
    tree['edges'][(best_attachment_vertex, best_vertex)] = best_cost
    remaining_vertices.remove(best_vertex)
  return tree    
  
def solve(filename):
  matrix = read_matrix(filename)
  matrix_cost = cost(matrix)
  tree = minimum_spanning_tree(matrix)
  tree_cost = cost(tree)
  savings = matrix_cost - tree_cost
  return savings

print(solve('problem107_data.txt'))
