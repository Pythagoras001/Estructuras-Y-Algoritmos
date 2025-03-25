# Creamos el dfs
def dfs(ini):
    recorrido.append(ini)
    visita[ini] = 1
    for vecino in conec[ini]:
        if visita[vecino]:
            return -1
        if dfs(vecino) == -1:
            return -1
    return 0

for _ in range(int(input())):
    # Recibimos la entrada
    n = int(input())
    est = list(map(int, input().split()))

    conec = [[] for _ in range(n+1)]
    pas = set()

    for i in range(n-1):
        conec[i].append(i+1)
        pas.add(i+1)

    for i in range(n):
        if not est[i]:
            conec[i].append(n)
            pas.add(n)
        else:
            conec[n].append(i)
            pas.add(i)

    # Buscamos un inicio 
    ini = (((n*(n+1)))//2) - sum(pas)

    if len(pas) == n+1:
        maxx = 0
        for i in range(len(conec)):
            if len(conec[i]) > maxx:
                ini = i
                maxx = len(conec[i])

    # Creamos una matriz de visitas
    visita = [0]*(n+1)
    recorrido = []

    # Aplicamos el dfs
    if dfs(ini) == -1:
        print(-1)
    else:
        print(recorrido)