from collections import deque

# Creamos el Bfs
def bfs(ini, disponi):
    q = deque()
    q.append(ini)
    visita[ini[0]][ini[1]] = 1
    disponi -= k+1

    movx = [1, -1, 0, 0]
    movy = [0, 0, 1, -1]

    while q:
        act = q.popleft()

        for i in range(4):
            nx = act[1] + movx[i]
            ny = act[0] + movy[i]

            if nx == m or ny == n or nx < 0 or ny < 0: continue
            if visita[ny][nx] == 1 or tablero[ny][nx] == '#': continue

            if disponi == 0:
                tablero[ny][nx] = 'X'
            else:
                disponi -= 1

            q.append([ny, nx])
            visita[ny][nx] = 1

# Recibimos la entrada
n, m, k = list(map(int, input().split()))

tablero = []
for _ in range(n):
    tablero.append(list(input()))

# Creamos un registro de visitas
visita = [[0]*m for _ in range(n)]

# Aplicaomos el Bfs
c = 0

for y in range(n):
    for x in range(m):
        if tablero[y][x] == '.':
            inicio = [y, x]
            c += 1

bfs(inicio, c)
for i in range(n):
    print(''.join(tablero[i]))