# Creamos el dfs
def dfs(ini):
    c = num[ini]-1
    pila = [(ini, ini)]

    while c > 0 :
        y, x = pila.pop()

        for i in range(4):
            ny = y + movy[i]
            nx = x + movx[i]

            if ny < 0 or ny == n: continue
            if nx < 0 or nx == len(tablero[ny]): continue

            if tablero[ny][nx] == -1:
                pila.append((ny, nx))
                tablero[ny][nx] = num[ini]
                c -= 1
                break

# Recibimos la entrada
n = int(input())
num = list(map(int, input().split()))

tablero = []
for i in range(1, n+1):
    fila = [-1]*i
    fila[-1] = num[i-1]

    tablero.append(fila)

# Definimos los movimientos
movx = [-1, 0, 1, 0 ]
movy = [0, 1, 0, -1]

# Aplicamos el dfs
for i in range(n):
    dfs(i)

for fila in tablero:
    print(*fila)