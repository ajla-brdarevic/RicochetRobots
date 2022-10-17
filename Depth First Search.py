graph = { #čvorovi u grafu
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

visited = set() #set koji prati koji čvorovi u grafu su posjećeni

def dfs(visited, graph, node):  
    if node not in visited:
        print (node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Dubinsko pretraživanje/Depth-First Search: ")
dfs(visited, graph, '1')