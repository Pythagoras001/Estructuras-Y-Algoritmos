from collections import deque

# Creamos el Bfs
def bfs(ini):
    q = deque()
    q.append(ini)

    if ini == obje:
        return 'YES'

    while q:
        act = q.popleft()

        if act % 3 == 0:
            q.append(act // 3)
            q.append((act // 3) * 2)

            if q[-1] == obje or q[-2] == obje:
                return 'YES'
    return 'NO'

# Aplicamos el Bfs
veces = int(input())

for _ in range(veces):
    oro, obje = list(map(int, input().split()))

    print(bfs(oro))