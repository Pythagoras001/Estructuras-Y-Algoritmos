# Creamos el dfs
def dfs(ini):
    pilaleft = [[ini, 0]]
    pilaright = [[ini, 0]]
    visitas[lista[ini]-1] = 1
    
    def valid(pila, r):
        if pila:
            index, prof = pila.pop()
            maxx = float('-inf')
            indexhijo = -1 
            fin = node
            salta = 1

            if r:
                salta = -1
                fin = -1
                index -= 2

            for i in range(index+1, fin, salta):
                if lista[i] > maxx and visitas[lista[i]-1] == 0:
                    maxx = lista[i]-1
                    indexhijo = i
                elif visitas[lista[i]-1] == 1:
                    break
            
            if indexhijo >= 0:
                visitas[maxx] = 1
                aws[indexhijo] = prof+1
                pilaleft.append([indexhijo, prof+1])
                pilaright.append([indexhijo, prof+1])

        return None

    while pilaright or pilaleft:
        valid(pilaright, False)
        valid(pilaleft, True)

# Recibimos la entrada
for _ in range(int(input())):
    node = int(input())
    lista = list(map(int, input().split()))
    aws = [0]*node

    # Creamos una lista de visitados
    visitas = [0]*node

    # Aplicamos el dfs
    dfs(lista.index(max(lista)))
    print(*aws)
