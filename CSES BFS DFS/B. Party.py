from collections import deque

def bfs(ini):
    q = deque()
    q.append(ini)
    visto[ini] = lista[ini]

    while q:
        act = q.popleft()
  
        for dest in conec[act]:
            if visto[dest] == -1:
                q.append(dest)
                visto[dest] = lista[dest]

# Recibimos la entrada
node, aris = map(int, input().split())
lista = list(map(int, input().split()))

conec = [[] for _ in range(node)]

for _ in range(aris):
    n1, n2 = map(int, input().split())

    conec[n1-1].append(n2-1)
    conec[n2-1].append(n1-1)

# Creamos una lista de visitas
visto = [-1]*node

# Aplicamos el bfs

for i in range(node):
    if visto[i] == -1:
        bfs(i)
        print(visto)

    

