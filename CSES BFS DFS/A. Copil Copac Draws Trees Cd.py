

# Creamos el bfs
def bfs(ini, apa):
    cola = [[ini, apa]]
    visto[ini] = 1
    maxx = 0
    c = 0
    while cola:
        act, level = cola.pop()
        
        for dest in conec[act]:
            if not visto[dest]:

                visto[dest] = 1
                pad, hijo = sorted([act, dest])

                if dicc[(pad, hijo)] > level:
                    c += 1
                
                cola.append([dest, dicc[(pad, level)]])

               
 

# Recibimos la entrada
node = int(input())

conec = [[] for _ in range(node)]
dicc = dict()
uno = float('inf')

for i in range(node-1):
    n1, n2 = sorted(list(map(int, input().split())))

    if 1 in [n1, n2]:
        uno = min(uno, i)

    dicc[(n1-1, n2-1)] = i

    conec[n1-1].append(n2-1)
    conec[n2-1].append(n1-1)

# Creamos un registro de visitas
visto = [0]*node

# Aplicamos el bfs

bfs(0, uno)