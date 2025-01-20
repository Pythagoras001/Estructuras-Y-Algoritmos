from collections import deque

# Creamos el bfs
def bfs(ini):
    q = deque()
    q.append(ini)
    dist[ini] = 1

    while q:
        act = q.popleft()

        for vinc in conec[act]:
            if dist[vinc] == -1:
                dist[vinc] = dist[act] + 1
                q.append(vinc)
                
    
    return None

# Recibimos la entrada
node, aris = list(map(int, input().split()))

conec = [[] for _ in range(node)]

for _ in range(aris):
    p1, p2 = list(map(int, input().split()))

    conec[p1-1].append(p2-1)
    conec[p2-1].append(p1-1)


# Creamos un registro de distancias
dist = list(map(int, ['-1']*node))

# Aplicamos el bfs
bfs(0)

if dist[-1] == -1:
    print("IMPOSSIBLE")
else:
    print(dist[-1])

    index = node-1
    his = [node]
    maxdist = dist[-1]-1

    while maxdist >= 1:
        for hisnode in conec[index]:
            if dist[hisnode] == maxdist:
                index = hisnode
                maxdist -= 1
                his.append(hisnode+1)
                break

    print(*his[::-1])
