import heapq as hq

# Creanmos el dj
def dj(ini):
    h = [(0, ini)]
    hq.heapify(h)
    esta[0] = 0

    ances = [-1]*(cant)
    
    while h:
        long, node =  hq.heappop(h)

        if long > esta[node]:
            continue

        for dest, d in distan[node]:
            if esta[dest] > long + d:
                esta[dest] = long+d
                hq.heappush(h, (long+d, dest))
                ances[dest] = node

    return ances

# Recibimos la entrada
cant, aris = map(int, input().split())

distan = [[]for _ in range(cant)]
for _ in range(aris):
    n1, n2, d = map(int, input().split())

    distan[n1-1].append([n2-1, d])
    distan[n2-1].append([n1-1, d])

# Cremos una lista de los estados
esta = [float('inf')]*cant

# Aplicamos el djw
aws = dj(0)

if aws[-1] < 0:
    print(-1)
else:
    i = aws[-1]
    r = [cant]

    while i != -1:
        r.append(i+1)
        i = aws[i]

    print(*r[::-1])