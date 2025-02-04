import heapq as hq

# Creamos el dfs
def dfs(ini):
    pila = [ini]
    hq.heapify(pila)

    visto[ini] = 1
    index = 0

    while pila:
        act = hq.heappop(pila)

        r[index] = act+1
        index += 1

        for dest in sorted(conecc[act], reverse=True):
            if not visto[dest]:
                visto[dest] = 1
                hq.heappush(pila, dest)

# Recibimos la entrada
node, aris = list(map(int, input().split()))

conecc = [[] for _ in range(node)]
for _ in range(aris):
    n1, n2 = list(map(int, input().split()))

    conecc[n1-1].append(n2-1)
    conecc[n2-1].append(n1-1)

# Creamos un registro de visitas
visto = [0]*node

# Creamos la respuesta
r = [0]*node

# Aplicamos el dfs
dfs(0)
print(*r)