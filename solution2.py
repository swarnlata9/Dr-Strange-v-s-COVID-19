def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
if __name__ == '__main__':
  line1 = input()
  l1 = line1.split(' ')
  n = int(l1[0])
  h = int(l1[1])
  x = int(l1[2])

  line2 = input()
  h_cities = line2.split(' ')

# import dictionary for graph
  from collections import defaultdict

  graph = {}
  for i in range(n-1):
      edge = input()
      e_list = edge.split(' ')
      if e_list[0] in graph.keys():
          graph[e_list[0]].append(e_list[1])
      else:
          graph[e_list[0]] = [e_list[1]]
        
      if e_list[1] in graph.keys():
          graph[e_list[1]].append(e_list[0])
      else:
          graph[e_list[1]] = [e_list[0]]
  possible_epicentres = []

  for node in graph.keys():
      flag = True
      for hotspot in h_cities:
          path = []
          path = find_path(graph, node, hotspot)
          if len(path)-1 > x:
              flag = False
    
      if flag:
          possible_epicentres.append(node)
  print(len(possible_epicentres))