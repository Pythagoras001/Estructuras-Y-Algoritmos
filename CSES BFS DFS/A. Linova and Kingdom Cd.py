import sys
sys.setrecursionlimit(300000)

# Creamos pruf
def pruf(ini, padre, y):
    contador = 0

    for dest in conecc[ini]:
        if dest != padre:
            contador += pruf(dest, ini, y+1) + 1
    
    dicc[ini] = [y, contador]
    hijos.append([contador, ini])
    return contador

# Creamos el medidor de felicidad
def feliz(ini):
    pila = [ini]
    visitas[ini] = 1
    c = 0

    while pila:
        act = pila.pop()

        if act in locat:
            c += dicc[act][0] * (dicc[act][1]+1)
            continue

        for dest in conecc[act]:
            if visitas[dest] != 1:
                pila.append(dest)
                visitas[dest] = 1

    return c

# Recibimos la entrada
node, indu = list(map(int, input().split()))

conecc = [[] for _ in range(node)]
for _ in range(node-1):
    c1, c2 = list(map(int, input().split()))

    conecc[c1-1].append(c2-1)
    conecc[c2-1].append(c1-1)

# Creamos un registro de hijos
hijos = []
visitas = [0]*node
dicc = dict()

# Aplicamos el pruf
pruf(0, -1, 0)
hijos.sort()

locat = set()

for i in range(node):
    if indu > 0:
        locat.add(hijos[i][1])
        indu -= 1
        continue
    break

print(feliz(0))