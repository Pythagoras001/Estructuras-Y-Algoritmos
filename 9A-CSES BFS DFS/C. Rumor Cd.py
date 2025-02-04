from collections import deque

# Creamos el bfs
def bfs(ini):
    q = deque()
    q.append(ini)
    visitas[ini] = 1

    while q:
        act = q.popleft()

        for desti in conecc[act]:
            if visitas[desti] == 0:
                visitas[desti] = 1
                q.append(desti)

# Recibimos la entrada
node, aris = list(map(int, input().split()))
costos = list(map(int, input().split()))
conecc = [[] for _ in range(node)]

order = []
for i in range(node): order.append([costos[i], i])
order.sort()

for _ in range(aris):
    a1, a2 = list(map(int, input().split()))

    conecc[a1-1].append(a2-1)
    conecc[a2-1].append(a1-1)

# Creamos una lista de visitas
visitas = [0]*node

# Aplicamos el Bfs
c = 0
for i in range(node):
    if visitas[order[i][1]] == 0:
        c += order[i][0]
        bfs(order[i][1])

print(c)