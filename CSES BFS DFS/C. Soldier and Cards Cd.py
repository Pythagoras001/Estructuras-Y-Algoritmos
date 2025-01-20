from collections import deque

# Creamos el bfs
def bfs(ini):
    j = 0
    g = 1
    visitas.add((tuple(p1), tuple(p2)))

    while p1 and p2:
        act1, act2 = p1.popleft(), p2.popleft()

        if act1 > act2:
            p1.append(act2)
            p1.append(act1)
        else:
            p2.append(act1)
            p2.append(act2)

        j += 1

        if not p1:
            g = 2

        if (tuple(p1), tuple(p2)) not in visitas:
            visitas.add((tuple(p1), tuple(p2)))
        else:
            return [-1] 
            
    return [j, g]

# Recibimos la entrada 
cant = int(input())
p1 = deque(map(int, input().split()[1:]))
p2 = deque(map(int, input().split()[1:]))

# Creamos un registro de visitas
visitas = set()

# Aplicamos el bfs
print(*bfs(0))