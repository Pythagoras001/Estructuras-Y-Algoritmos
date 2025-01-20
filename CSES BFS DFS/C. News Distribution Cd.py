from collections import deque

# Creamos el bfs
def bfs(ini, code):
    q = deque()
    q.append(ini)

    visto[ini] = code
    c = 1

    while q:
        act = q.popleft()

        for dest in conec[act]:
            if visto[dest] == 0:
                c += 1
                visto[dest] = code
                q.append(dest)
    
    repe[code] = c 
    return c

# Recibimos la entrada
node, group = list(map(int, input().split()))

conec = [[] for _ in range(node)]

for _ in range(group):
    lista = list(map(int, input().split()))
    
    for i in range(1, lista[0]):
        if lista[i+1]-1 not in conec[lista[i]-1]:
            conec[lista[i]-1].append(lista[i+1]-1)
            conec[lista[i+1]-1].append(lista[i]-1)

# Creamos un registro de vistos 
visto = [0]*node
repe = dict()

# Aplicamos el bfs
for i in range(node):
    if visto[i] == 0:
        print(bfs(i, i+1), end=' ')
    else:
        print(repe[visto[i]], end=' ')