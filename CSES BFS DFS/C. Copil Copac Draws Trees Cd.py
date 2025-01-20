from collections import deque

# Creamos el bfs
def bfs(ini, start, steps):
    q = deque()
    q.append([ini, start, steps])
    vistos[ini] = 1
    pruf = 1

    while q:
        ini, start, steps = q.popleft()

        for dest in conec[ini]:
            if not vistos[dest]:
                
                vistos[dest] = 1
                d1, d2 = sorted([ini, dest])

                if apar[(d1, d2)] < start:
                    q.append([dest, apar[(d1, d2)], steps + 1])
                    pruf = max(pruf, steps+1)

                else:
                    q.append([dest, apar[(d1, d2)], steps])

    return pruf

# Recibimos la entrada
for _ in range(int(input())):
    node = int(input())

    conec = [[] for _ in range(node)]
    apar = dict()
    orig = -1

    for i in range(node-1):
        n1, n2 = sorted(list(map(int, input().split())))
        apar[(n1-1, n2-1)] = i 

        if n1 == 1 and orig == -1:
            orig = i

        conec[n2-1].append(n1-1)
        conec[n1-1].append(n2-1)

    # Creamos un registro de vistos
    vistos = [0]*node

    # Aplicamos el bfs
    print(bfs(0, orig, 1))