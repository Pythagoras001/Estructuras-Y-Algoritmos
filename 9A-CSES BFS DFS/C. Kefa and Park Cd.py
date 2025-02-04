from collections import deque

# Creamos el Bfs
def bfs(ini):
    q = deque()
    q.append([ini, estado[ini]])
    visita[ini] = 1
    c = 0

    while q:
        act = q.popleft()

        if len(conecc[act[0]]) == 1 and act[0] != 0:
            c += 1

        for dest in conecc[act[0]]:
            if visita[dest] == 0:
                if estado[dest] == 0:
                    q.append([dest, 0])

                elif act[1] + estado[dest] <= tole:
                    q.append([dest, act[1] + estado[dest]])

                visita[dest] = 1

    return c

# Recibimos la entrada
node, tole = list(map(int, input().split()))
estado = list(map(int, input().split()))

conecc = [[] for _ in range(node)]
for _ in range(node-1):
    r1, r2 = list(map(int, input().split()))

    conecc[r1-1].append(r2-1)
    conecc[r2-1].append(r1-1)

# Lista de visitados
visita = [0]*node

# Aplicamos el bfs
print(bfs(0))