# Creamos el dfs
def dfs(x, y):
    pilax = [x]
    pilay = [y]

    while pilay or pilax:
        if pilax:
            actualx = pilax.pop()
            for x in ubicax[actualx]:
                if visita[x[2]][0] == 0:
                    pilay.append(x[1])
                    visita[x[2]][0] = 1

        if pilay:  
            actualy = pilay.pop()
            for y in ubicay[actualy]:
                if visita[y[2]][1] == 0:
                    pilax.append(y[0])
                    visita[y[2]][1] = 1

# Recibimos la entrada
cant = int(input())

ubicax = dict()
ubicay = dict()
regist = []

for n in range(cant):
    dat = list(map(int, input().split()))
    regist.append(dat)

    if dat[0] not in ubicax:
        ubicax[dat[0]] = [dat + [n]]
    else:
        ubicax[dat[0]].append(dat + [n])

    if dat[1] not in ubicay:
        ubicay[dat[1]] = [dat + [n]]
    else:
        ubicay[dat[1]].append(dat + [n])

# Creamos un registro de visitas
visita = [[0, 0] for _ in range(cant)]

# Aplicamos el dfs
c = 0
for i in range(cant):
    if visita[i] == [0, 0]:
        dfs(regist[i][0], regist[i][1])
        c += 1

# Imprimimos el resultado
print(c - 1)
