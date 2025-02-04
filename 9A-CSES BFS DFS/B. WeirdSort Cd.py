# Creamos el dfs
def dfs(ini):
    pila = [ini]
    visita[ini] = 1
    r = []

    while pila:
        act = conecc[pila.pop()]

        if len(act) == 1:
            r.append(act[0])
        
        else:
            visita[act[1]] = 1
            pila.append(act[1])
            r.append(act[0])
        
    return max(r), min(r)

# Recibimos la entrada
for _ in range(int(input())):
    node, aris = list(map(int, input().split()))
    a = list(map(int, input().split()))
    p = set(map(int, input().split()))

    conecc = []
    for n in range(node):
        if n+1 in p:
            conecc.append([a[n]-1, n+1])
        else:
            conecc.append([a[n]-1])

    # Creamos una lista de visitados
    visita = [0]*node

    # Aplicamos el dfs
    ulti = -1
    accep = 'YES'

    for i in range(node):
        if visita[i] == 0:
            maxx, minn = dfs(i)
        
            if ulti <= minn:
                ulti = maxx
                continue
            accep = 'NO'

    print(accep)

