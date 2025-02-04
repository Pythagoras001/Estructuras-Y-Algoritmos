# Creamos el dfs
def dfs(ini, mov):
    pila = [(ini, mov)]
    r = []
    cant = 0
    visit = set()

    while pila:
        act = pila.pop()

        if act in visit:
            continue
        else:
            visit.add(act)

        if act[1] == aris:
            r.append(act[0])
            cant += 1
            continue

        if tiros[act[1]][1] in ['0', '?']:
            der = act[0]+int(tiros[act[1]][0])
            if der > node:
                der %= node
            pila.append((der, act[1]+1))

        if tiros[act[1]][1] in ['1', '?']:
            iz = act[0]-int(tiros[act[1]][0])
            if iz < 1:
                iz += node
            pila.append((iz, act[1]+1))
    
    print(cant)
    return r

# Recibimos la entrada
for _ in range(int(input())):
    node, aris, ini = list(map(int, input().split()))

    tiros = []
    for _ in range(aris):
        tiros.append(input().split())

    # Alicamos el dfs
    print(*sorted(dfs(ini, 0)))