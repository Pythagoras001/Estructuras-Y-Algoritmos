# Creamos el dfs
def dfs(ini):
    pila = [[ini, ini]]
    visitas[ini[0]][ini[1]] = 1

    movy = [1, -1, 0, 0]
    movx = [0, 0, -1, 1]

    while pila:
        ulti = pila.pop()
        act = ulti[0]
        padre = ulti[1]

        for i in range(4):
            ny = act[0] + movy[i]
            nx = act[1] + movx[i]

            if ny == n or nx == m or ny < 0 or nx < 0: continue
            if [ny, nx] == padre or tablero[ny][nx] != tablero[ini[0]][ini[1]]: continue 

            if visitas[ny][nx] == 1:
                return True

            visitas[ny][nx] = 1
            pila.append([[ny, nx], act])

    return False

# Recibimos la entrada
n, m = list(map(int, input().split()))

tablero = []
for _ in range(n):
    tablero.append(input())

# Creamos un registro de vivistas
visitas = [[0]*m for _ in range(n)]

# Aplicamos el dfs
r = 'No'
for y in range(n):
    if r == 'Yes': break

    for x in range(m):
        if visitas[y][x] == 0:
            if dfs([y, x]):
                r = 'Yes'
                break

print(r)