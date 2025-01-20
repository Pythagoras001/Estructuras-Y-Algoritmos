def dfs(inix, iniy, visitados, tablero):
    ylimit = len(tablero)
    xlimit = len(tablero[0])
    movx = [-1, 0, 0, 1]
    movy = [0, 1, -1, 0]

    pila = [(inix, iniy)]
    visitados[iniy][inix] = '1'

    while pila:
        x, y = pila.pop()

        for i in range(4):
            ejex = x + movx[i]
            ejey = y + movy[i]

            if ejex >= xlimit or ejey >= ylimit or ejey < 0 or ejex < 0:
                continue
            if tablero[ejey][ejex] == '#' or visitados[ejey][ejex] == '1':
                continue

            visitados[ejey][ejex] = '1'
            pila.append((ejex, ejey))

# Guardamos el tablero
n, m = list(map(int, input().split()))

tablero = []
for _ in range(n):
    tablero.append(input())

# Creamos el tablero de visitados
visitados = [list('0'*m) for _ in range(n)]

# Usamos el dfs en el tablero
c = 0
for y in range(n):
    for x in range(m):
        if visitados[y][x] == '0' and tablero[y][x] == '.':
            dfs(x, y, visitados, tablero)
            c += 1

print(c)

