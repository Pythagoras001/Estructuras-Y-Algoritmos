import heapq as hq

# Creamos el dj
def dj(ini):
    h = []
    hq.heapify(h)
    hq.heappush(h, (0, ini))

    while h:
        long, node = hq.heappop(h)

        if long > act[node]:
            continue

        for dest in conec[node]:
            op = long + distan[(node, dest)]

            if act[dest] > op:
                hq.heappush(h, (op, dest))
                act[dest] = op

# Recibimos la entrada
cant, aris = map(int, input().split())

conec = [[] for _ in range(cant)]
distan = dict()

for _ in range(aris): 
    n1, n2, d = map(int, input().split())

    distan[(n1-1, n2-1)] = min(d, distan.get((n1-1, n2-1), float('inf')))

    conec[n1-1].append(n2-1)

# Creamos las distancias actuales
act = [float('inf')]*cant
act[0] = 0

# Aplicamos el dj
dj(0)
print(*act)