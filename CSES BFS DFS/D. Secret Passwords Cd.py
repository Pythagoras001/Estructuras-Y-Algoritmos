# Cramos el dfs
def dfs(ini):
    pila = [ini]
    visita[ini] = 1
    
    while pila:
        act = pila.pop()

        for dest in conecc[act]:
            if visita[dest] == 0:
                visita[dest] = 1
                pila.append(dest)


# Recibimos la entrada
node = int(input())

conecc = [[] for _ in range(node)]
ubic = dict()

for i in range(node):
    code = input()
    parent = set()

    for item in code:

        if item in ubic and ubic[item] != i and ubic[item] not in parent:
            conecc[ubic[item]].append(i)
            conecc[i].append(ubic[item])
            parent.add(ubic[item])
        else:
            ubic[item] = i

# Creamos un registro de visitas
visita = [0]*node

# Aplicamos el dfs
c = 0
for i in range(node):
    if visita[i] == 0:
        dfs(i)
        c += 1

print(c)