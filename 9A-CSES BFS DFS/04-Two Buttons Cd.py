from collections import deque

# Creamos el Bfs
def bfs(ini):
    q = deque()
    q.append([ini, 0])
    regis.add(ini)

    while q:
        act = q.popleft()

        if act[0]*2 not in regis and act[0] < obj:
            q.append([act[0]*2, act[1]+1])
            regis.add(act[0]*2)
            if act[0]*2 == obj:
                return act[1]+1

        if act[0]-1 not in regis and act[0]-1 > 0:
            q.append([act[0]-1, act[1]+1])
            regis.add(act[0]-1)
            if act[0]-1 == obj:
                return act[1]+1

    return 0

# Recibimos la entrada
est, obj = list(map(int, input().split()))
regis = set()

print(bfs(est))
