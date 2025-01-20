from collections import deque

# Creamos el bfs
def bfs(ini, his):
    q = deque()
    q.append([ini, his])
    visita[ini] = 1
    dicc[ini] = 0

    while q:
        act, pas = q.popleft()

        for dest in conec[act]:
            if not visita[dest]:
                visita[dest] = 1
                dicc[dest] = pas + 1
                q.append([dest, pas+1])

# Recibimos la entrada 
node = int(input())

conec = [[] for _ in range(node)]
hijos = [set() for _ in range(node)]

for _ in range(node-1):
    n1, n2 = list(map(int, input().split()))

    conec[n1-1].append(n2-1)
    conec[n2-1].append(n1-1)

    hijos[n1-1].add(n2-1)
    hijos[n2-1].add(n1-1)

dicc = dict()
order = list(map(int, input().split()))

for elem in order:
    dicc[elem-1] = -1

# Creamos un registro de visitas
visita = [0]*node

# Aplicamos el bfs
bfs(0, 0)

# Aplicamos un two pointers para validar a los hijos
iz = 0
der = 1
r = 'Yes'

while iz <= der and r == 'Yes' and der <= node-1:
    if dicc[order[iz]-1] >= dicc[order[der]-1]:
        r = 'No'
        break
    
    if order[der]-1 in hijos[order[iz]-1]:
        der += 1
    else:
        iz += 1

print(r)