from collections import deque

# Creamos el bfs
def bfs(ini):
    q = deque()
    q.append(ini)
    r = [ini]

    while q:
        act = q.popleft()

        if act % 3 == 0 and act // 3 in exis:
            r.append(act//3)
            q.append(act//3)

        elif act*2 in exis:
            r.append(act*2)
            q.append(act*2)

    return r

# Recibimos la entrada
cant = int(input())

lista = list(map(int, input().split()))
exis = set(lista)

#Aplicamos el bfs
for i in range(cant):
    r = bfs(lista[i])
    if len(r) == cant:
        print(*r)

