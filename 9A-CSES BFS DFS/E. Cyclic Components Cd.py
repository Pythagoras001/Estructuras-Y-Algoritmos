

# Creamos el Dfs
def dfs(ini):
    q = [[ini, -1]]
    visitas[ini] = True  
    ciclo = True  

    while q:
        act, padre = q.pop()

        if len(conecc[act]) != 2:
            ciclo = False

        for desti in conecc[act]:
            if not visitas[desti]:
                visitas[desti] = True
                q.append([desti, act])
            elif desti != padre:  
                continue
  
    return ciclo 

# Recibimos la entrada
node, aris = list(map(int, input().split()))

conecc = [[] for _ in range(node)]
for _ in range(aris):
    n1, n2 = list(map(int, input().split()))

    conecc[n1-1].append(n2-1)
    conecc[n2-1].append(n1-1)

# Creamos una lista de visitas
visitas = [0]*node

c = 0
for i in range(node):
    if visitas[i] == 0:
        if dfs(i):
            c += 1

print(c)