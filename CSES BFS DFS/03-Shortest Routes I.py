import heapq

def dijkstra(ini):
    pq = []
    visita[ini] = 0
    heapq.heappush(pq, (0, ini))  # (distancia acumulada, nodo actual)

    while pq:
        dist_actual, act = heapq.heappop(pq)

        # Si ya procesamos un nodo con menor distancia, lo ignoramos
        if dist_actual > visita[act]:
            continue

        for dest in conecc[act]:
            nueva_dist = dist_actual + distan[(act, dest)]
            if nueva_dist < visita[dest]:
                visita[dest] = nueva_dist
                heapq.heappush(pq, (nueva_dist, dest))

# Entrada
node, aris = map(int, input().split())
conecc = [[] for _ in range(node)]
distan = dict()

for _ in range(aris):
    c1, c2, p = map(int, input().split())
    conecc[c1-1].append(c2-1)
    distan[(c1-1, c2-1)] = min(p, distan.get((c1-1, c2-1), float('inf')))

# Inicializamos distancias
visita = [float('inf')] * node

# Ejecutamos Dijkstra desde el nodo 0
dijkstra(0)

# Imprimimos las distancias
for i in range(node):
    print(visita[i], end=' ')