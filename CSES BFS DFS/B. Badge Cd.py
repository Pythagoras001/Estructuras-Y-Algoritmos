node = int(input())
lista = list(map(int, input().split()))

for i in range(node):
    visitas = [0]*node
    pila = [lista[i]-1]
    visitas[i] = 1
   
    while pila:
        act = pila.pop()
        
        if visitas[act]:
            print(act+1, end=' ')
            continue

        visitas[act] = 1
        pila.append(lista[act]-1)