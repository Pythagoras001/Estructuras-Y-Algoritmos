from collections import deque

# Creamos el bfs
def bfs(ini):
    q = deque()
    movx = [1, -1, 0, 0]
    movy = [0, 0, 1, -1]

    q.append(ini)
    visita[ini[0]][ini[1]] = 1
    c = tablero[ini[0]][ini[1]]

    while q:
        act = q.popleft()

        for i in range(4):
            ny = act[0] + movy[i]
            nx = act[1] + movx[i]

            if ny == n or nx == m or ny < 0 or nx < 0 : continue
            if visita[ny][nx] == 1 or tablero[ny][nx] == 0 : continue

            c += tablero[ny][nx]
            visita[ny][nx] = 1
            q.append([ny, nx])

    return c

# Recibimos la entrada
veces = int(input())

for _ in range(veces):
    n, m = list(map(int, input().split()))

    tablero = []
    for _ in range(n):
        tablero.append(list(map(int, input().split()))) 

    # Creamos un registro de visitas
    visita = [[0]*m for _ in range(n)]

    # Aplicamos el bfs
    cant = [0]
    for y in range(n):
        for x in range(m):
            if visita[y][x] == 0 and tablero[y][x] > 0:
                cant.append(bfs([y, x]))
                
    print(max(cant))