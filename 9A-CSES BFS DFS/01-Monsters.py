from collections import deque

# Creamos el bfs
def bfs(ini):
    q.append(ini)
    mox = [1, -1, 0, 0]
    moy = [0, 0, 1, -1]

    while q:
        act = q.popleft()

        for i in range(4):
            ny = act[0] + moy[i]
            nx = act[1] + mox[i]
        
            if ny == n or nx == m or ny < 0 or nx < 0: continue
            if tablero[ny][nx] == '#' or visita[ny][nx] != -1 : continue

            if visita[act[0]][act[1]] == 0:
                visita[ny][nx] = 0
            else:
                visita[ny][nx] = visita[act[0]][act[1]] + 1
    
            q.append([ny, nx])

# Creamos una funcion para reconstruir el camino
def reconstruccion(ini):
    mox = [1, -1, 0, 0]
    moy = [0, 0, 1, -1]
    direcc = ['L', 'R', 'U', 'D']
    awr = []

    act = visita[ini[0]][ini[1]] -1

    while act > 0:

        for i in range(4):
            ny = ini[0] + moy[i]
            nx = ini[1] + mox[i]
            
            if ny == n or nx == m or ny < 0 or nx < 0: continue

            if visita[ny][nx] == act:
                awr.append(direcc[i])
                ini = [ny, nx]
                act -= 1
                break

    return awr

# Recibimos la entrada Y gurdamos las posibles salidas
n, m = list(map(int, input().split()))

q = deque()
tablero = []
salida = []

visita = [[-1]*m for _ in range(n)]

for i in range(n):
    code = input()
    tablero.append(code)

    for f in range(m):
        if i == 0 or i == n-1:
            if code[f] in ['.', 'A'] : salida.append([i, f])
        elif f == 0:
            if code[-1] in ['.', 'A']: salida.append([i, m-1])
            if code[0] in ['.', 'A']: salida.append([i, 0])

        if code[f] == 'M':
            q.append([i, f])
            visita[i][f] = 0
        
        elif code[f] == 'A':
            user = [i, f]
            visita[i][f] = 1

# Aplicamos el Bfs apartir del usuario
bfs(user)
p = True

for candi in salida:
    if visita[candi[0]][candi[1]] > 0:
        print(f'YES \n{visita[candi[0]][candi[1]]-1}')
        print(''.join(reconstruccion(candi)[::-1]))
        p = False
        break

if p:
    print('NO')