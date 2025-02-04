# Creamos el dfs
def dfs(ini, code):
    pila = [ini]
    visto[ini] = code
    c = 1

    while pila:
        act = pila.pop()

        if visto[lista[act]-1] == 0:
            c += 1
            visto[lista[act]-1] = code
            pila.append(lista[act]-1)
    
    regis[code] = c
    return c

# Recibimos la entrada
for _ in range(int(input())):
    node = int(input())
    lista = list(map(int, input().split()))

    # Creamos un registro de vistos
    visto = [0]*node
    regis = dict()

    # Aplicamos el dfs
    for i in range(node):
        if visto[i] == 0:
            print(dfs(i, i+1), end=' ')
        else:
            print(regis[visto[i]], end=' ')

    print('')