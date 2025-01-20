from collections import deque

# Creamos el bfs
def bfs(ini):
    q = deque()
    q.append(ini)
    grupo[ini] = 2

    while q:
        act = q.popleft()

        for amigo in conec[act]:
            if grupo[amigo] != grupo[act] and grupo[amigo] == 0:
                grupo[amigo] = (grupo[act]%2) + 1
                q.append(amigo)
            elif grupo[amigo] == grupo[act]:
                return True

    return False

# Recibimos los entrada
node, aris = list(map(int, input().split()))

conec = [[] for _ in range(node)]

for _ in range(aris):
    a1, a2  = list(map(int, input().split()))

    conec[a1-1].append(a2-1)
    conec[a2-1].append(a1-1)

# Creamos el grupo en el que perteneceran
grupo = [0]*node

# Aplicamod el bfs
r = True

for i in range(node):
    if grupo[i] == 0:
        if bfs(i):
            print('IMPOSSIBLE')
            r = False
            break

if r:
    print(*grupo)
