from collections import deque

# Creamos el bfs
def bfs(ini):
    visit[ini] = '1'
    d = deque()
    d.append(ini)

    while d:
        act = d.popleft()
        for dest in conec[act]:
            if visit[dest] != '1':
                visit[dest] = '1'
                d.append(dest)
 
# Recibimos los datos

node, aris = list(map(int, input().split()))

conec = [[] for _ in range(node)]

for _ in range(aris):
    c1, c2 = list(map(int, input().split()))

    conec[c1-1].append(c2-1)
    conec[c2-1].append(c1-1)

# Creamos un registro de visitas

visit = ['0']*node

# Aplicamos el bfs 
c = 0
newConec = []
for i in range(node):
    if visit[i] != '1':
        bfs(i)
        c += 1
        if i > 0:
            newConec.append([1, i+1])

# Imprimimos los resultados
print(c-1)
for i in range(c-1):
    print(*newConec[i])