# Creamos el dfs
def bfs(ini):
    for elemen in conecc[ini]:
        if len(conecc[elemen]) > 1:
            return len(conecc[elemen])

# Recibimos la entrada
for _ in range(int(input())):
    node, arist = list(map(int, input().split()))

    conecc = [[] for _ in range(node)]
    for _ in range(arist):
        n1, n2 = list(map(int,input().split()))

        conecc[n1-1].append(n2-1)
        conecc[n2-1].append(n1-1)

    # Aplicamos el bfs
    for i in range(node):
        if len(conecc[i]) == 1:
            y = len(conecc[conecc[i][0]])-1
            x = bfs(conecc[i][0])
            break
        
    print(x, y)