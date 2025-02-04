# Creamos el dfs
def dfs(y, x):
    ult = [y, x]
    pila = [[y, x]]
    visitas[x] = 1

    while pila:
        act = pila.pop()
        act[0] += 1

        if act[0] == n:
            break

        if tablero[act[0]][act[1]] == 'o':
            ult = -1

        if tablero[act[0]][act[1]] == '*' and ult == -1:
            ult = [act[0], act[1]]
            y = act[0]

        elif tablero[act[0]][act[1]] == '.' and ult != -1:
            tablero[act[0]][act[1]] = '*'
            tablero[y][x] = '.'
            y += 1

        pila.append(act)
        
# Recibimos la entrada
for _ in range(int(input())):
    n, m = list(map(int, input().split()))

    tablero = []
    for _ in range(n):
        tablero.append(list(input()))

    # Creamos un registro de visitas
    visitas = [0]*m

    # Aplicamos el dfs
    for s in range(n):
        for i in range(m):
            if tablero[s][i] == '*' and visitas[i] == 0:
                dfs(s, i)   

    for eje in tablero:
        print(''.join(eje))