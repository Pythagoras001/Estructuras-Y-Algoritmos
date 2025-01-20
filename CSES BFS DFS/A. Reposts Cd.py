# Creamos el dfs
def dfs(ini):
    pila = [ini]
    maxx = 1

    while pila:
        act = pila.pop()

        for dest in conecc[act[0]]:
            pila.append([dest, act[1]+1])
            if act[1]+1 > maxx:
                maxx = act[1]+1

    return maxx

# Recibimos la entrada
cant = int(input())
dicc = dict()
c = 0

conecc = []
for _ in range(cant):
    n1, code, n2 = input().lower().split()

    if n1 not in dicc: 
        dicc[n1] = c
        c += 1
        conecc.append([])

    if n2 not in dicc:
        dicc[n2] = c
        c += 1
        conecc.append([])

    conecc[dicc[n2]].append(dicc[n1])

# Aplicamos el dfs
print(dfs([dicc['polycarp'], 1]))