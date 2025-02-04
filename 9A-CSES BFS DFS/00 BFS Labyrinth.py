from collections import deque

# Creamos el dfs
def bfs(iniy, inix, c, f):

    cola = deque()
    cola.append([iniy, inix]) 
    dist[iniy][inix] = 0
    movx = [1, 0, 0, -1]
    movy = [0, 1, -1, 0]

    while cola:
        act = cola.popleft()
        for i in range(4):
            ny = act[0] + movy[i]
            nx = act[1] + movx[i]

            if ny >= c or nx >= f or ny < 0 or nx < 0:
                continue
            if dist[ny][nx] != -1 or tablero[ny][nx] == '#':
                continue

            dist[ny][nx] = dist[act[0]][act[1]] + 1
            cola.append([ny, nx])

# Creamos la reeconstruccion del retorno
def devuelta(iniy, inix, prof, c, f):
    movx = [1, 0, 0, -1]
    movy = [0, 1, -1, 0]
    direc = ['L', 'U', 'D', 'R']
    act = prof-1
    r = []
 
    while act >= 0:
        for i in range(4):
            ny = iniy + movy[i]
            nx = inix + movx[i]

            if ny >= c or nx >= f or ny < 0 or nx < 0:
                continue
            if dist[ny][nx] == act:
                r.append(direc[i])
                act -= 1
                iniy = ny
                inix = nx
                break
    return r

# Recivimos las varialbles
c, f = list(map(int, input().split()))

tablero = [] 
for _ in range(c):
    tablero.append(input())

# Creamos el mapa de distancias
dist = [list(map(int, ['-1']*f)) for _ in range(c)]

# Aplicamos el dfs
for y in range(c):
    for x in range(f):
        if tablero[y][x] == 'A':
            bfs(y, x, c, f)

        if tablero[y][x] == 'B':
            finy, finx = y, x 

if dist[finy][finx] == -1:
    print('NO')
else:
    print('YES')
    print(dist[finy][finx])
    print(''.join(devuelta(finy, finx, dist[finy][finx], c, f)[::-1]))