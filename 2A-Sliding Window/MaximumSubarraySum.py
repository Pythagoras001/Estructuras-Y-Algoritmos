cant = int(input())
lista = list(map(int, input().split()))

inicio = 0
suma = 0
maxsuma = lista[0]

for fin in range(cant):
    if cant == 1:
        break

    suma += lista[fin]
    
    if lista[fin] >= 0:
        if lista[inicio+1] > 0 and lista[inicio] < 0:
            suma -= lista[inicio]
            inicio += 1

    if lista[fin] >= suma:
        inicio = fin
        suma = lista[fin]

    maxsuma = max(maxsuma, suma)

print(maxsuma)

