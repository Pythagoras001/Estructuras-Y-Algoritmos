# Creamos el dfs
def dfs(ini):
    movx = [1, -1, 0, 0]
    movy = [0, 0, 1, -1]
    
    q = [ini]
    visitas[ini[0]][ini[1]] = 1

    while q:
        act = q.pop()

        for i in range(4):
            ny = act[0] + movy[i]
            nx = act[1] + movx[i]

            if nx == m or ny == 2 or nx < 0 or ny < 0: continue

            nx += 1
            if tablero[ny][nx-1] == '<':
                nx -= 2
            
            if visitas[ny][nx] == 1: continue

            q.append([ny, nx])
            visitas[ny][nx] = 1

# Recibimos la entrada
for _ in range(int(input())):
    m = int(input())

    tablero = []
    for _ in range(2):
        tablero.append(input())

    # Creamos un registro de visitas
    visitas = [[0]*m  for _ in range(2)]

    # Aplicamos el bfs
    dfs([0 ,0])

    r = 'NO'
    if visitas[1][-1] == 1:
        r = 'YES'

    print(r)