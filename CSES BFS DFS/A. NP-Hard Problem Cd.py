# Creamos el dfs
def dfs(ini):
    pila = [[ini,-1, 0]]
    visto[ini] = 0

    while pila:
        act, pad, grup = pila.pop()

        if grup:
            a1.append(act+1)
        else:
            a2.append(act+1)

        for dest in conecc[act]:
            if grup == visto[dest]:
                return -1
            elif visto[dest] == -1:
                pila.append([dest, act, (grup+1)%2])
                visto[dest] = (grup+1)%2

    return a1, a2

# Recibimos la entrada 
node, aris = list(map(int, input().split()))

conecc = [[] for _ in range(node)]
for _ in range(aris):
    n1, n2 = list(map(int, input().split()))

    conecc[n1-1].append(n2-1)
    conecc[n2-1].append(n1-1)

# Creamos un registro de visitas
visto = [-1]*node
a1 = []
a2 = []

# Aplicamos el dfs
r = True
for i in range(node):
    if visto[i] == -1:
        if len(conecc[i]) > 0:
            a = dfs(i)

            if a == -1:
                r = False
                break

if r:
    print(len(a2))
    print(*a2)
    print(len(a1))
    print(*a1)
    
else:
    print(-1)
