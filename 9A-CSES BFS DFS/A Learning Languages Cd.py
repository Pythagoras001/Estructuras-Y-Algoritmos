from collections import deque

# Creamos el bfs
def bfs(ini):
    q = deque()
    q.append(ini)
    visitado[ini] = 1

    while q:
        act = q.popleft()

        for dest in conocimi[act]:
            for i in range(nodes):
                if dest in conocimi[i] and visitado[i] == 0:
                    visitado[i] = 1
                    q.append(i)
    return None

# Recibimos la entrada
nodes, idioms = list(map(int, input().split()))
conocimi = []

for i in range(nodes):
    lista = set(map(int, input().split()[1:]))
    conocimi.append(lista)

# Creamos una lista de visitados
visitado = [0]*nodes

# Aplicamos el bfs
aclopa = False
c = 0
for i in range(nodes):
    if len(conocimi[i]) > 0:
        aclopa = True
    if visitado[i] == 0:
        bfs(i)
        c += 1

if aclopa:
    c -= 1
print(c)
