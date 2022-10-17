graph = { #cvorovi u grafu
  '1' : ['2','10', '13'],
  '2' : ['3', '6'],
  '3' : ['4', '5'],
  '4' : [],
  '5' : [],
  '6' : ['7', '8', '9'],
  '7' : [],
  '8' : [],
  '9' : [],
  '10' : ['11', '12'],
  '11' : [],
  '12' : [],
  '13' : ['14', '15', '16'],
  '14' : [],
  '15' : [],
  '16' : [],
}

visited = [] # Lista set koji prati koji cvorovi u grafu su posjeceni
queue = []     #inicijalizacija reda čekanja

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Obilazak po širini/Breadth-First Search: ")
bfs(visited, graph, '1')