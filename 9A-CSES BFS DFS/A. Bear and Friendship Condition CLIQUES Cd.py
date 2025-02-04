
# Creamos el dfs
def dfs(ini):
    pila = [[ini, -1]]  
    visita[ini] = 1
    nodes = 1  
    arista = 0  

    while pila:
        act, padre = pila.pop()

        for dest in conecc[act]:
            arista += 1 
            if dest == padre:
                continue  

            if not visita[dest]:
                pila.append((dest, act))
                visita[dest] = 1
                nodes += 1

    arista //= 2  
    return nodes, arista

# Recibimos la entrada
n, m = list(map(int, input().split()))

conecc = [[] for _ in range(n)]
for _ in range(m):
    a1, a2 = list(map(int, input().split()))

    conecc[a1-1].append(a2-1)
    conecc[a2-1].append(a1-1)

# Creamos una matriz de visitados
visita = [0] * n

# Aplicamos el dfs
z = 'YES'
for i in range(n):
    if visita[i] == 0:
        nodes, arista = dfs(i)

        if arista != nodes * (nodes - 1) // 2:
            z = 'NO'
            break

print(z)


