# Creamos el dfs
def dfs(ini):
    cola = [(ini, 0)]
    visit[ini] = 1
    
    while cola:
        act, g = cola.pop()

        for dest in conec[act]:
            if not visit[dest]:
                grupos[(g+1)%2].append(dest)
                cola.append((dest, (g+1)%2))
                visit[dest] = 1

    return grupos

# Recibimos la entrada
node = int(input())

conec = [[] for _ in range(node)]
for _ in range(node-1):
    n1, n2 = map(int, input().split())

    conec[n1-1].append(n2-1)
    conec[n2-1].append(n1-1)

# Creamos una lista de visitas y diccionario de grupos
grupos = {0:[0], 1:[]}
visit = [0]*node

# Aplicamos el dfs
dfs(0)

c = len(grupos[1])
aws = 0

for elemen in grupos[0]:
    aws += c - len(conec[elemen])

print(aws)