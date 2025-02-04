from collections import deque

# Creamos el bfs
def bfs(ini):
    cola = deque()
    cola.append(ini)
    visitas[ini[0]][ini[1]] = 1
    c = 1

    while cola:
        act = cola.popleft()

        for i in range(4):
            ny = act[0] + movy[i]
            nx = act[1] + movx[i]

            if ny == n or nx == m or ny < 0 or nx < 0: continue
            if visitas[ny][nx] == 1 or tablero[ny][nx] == '#': continue

            if tablero[ny][nx] == 'G':
                c += 1

            visitas[ny][nx] = 1
            cola.append([ny, nx])

    return c

# Recibimos la entrada
for _ in range(int(input())):
    n, m = list(map(int, input().split()))

    tablero = []
    good = []
    bad = []
    r = 'YES'

    for y in range(n):
        tablero.append(list(input()))

        for x in range(m):
            if tablero[-1][x] == 'B':
                bad.append([y, x])
            elif tablero[-1][x] == 'G':
                good.append([y, x])

    # Establecemos los m ovimientos
    movy = [1, -1, 0, 0]
    movx = [0, 0, 1, -1]
    posi = True

    # Encerramos los malos
    for y, x in bad:
        for i in range(4):
            ny = y + movy[i]
            nx = x + movx[i]

            if ny == n or nx == m or ny < 0 or nx < 0: continue
            if tablero[ny][nx] == 'B': continue
            elif tablero[ny][nx] == 'G':
                posi = False
                continue

            tablero[ny][nx] = '#'

    # Creamos un registro de visitas
    visitas = [[0]*m for _ in range(n)]

    # Aplicamos el bfs
    if len(good) == 0 or bfs(good[0]) == len(good) and visitas[-1][-1] == 1 and posi: 
        print('Yes')
    else:
        print('No')