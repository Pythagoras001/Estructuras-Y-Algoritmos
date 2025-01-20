veces = int(input())
lista = sorted(list(map(int, input().split())))

ini = 0
maxx = lista[0] + 5

c = 1
suma = 1

for fin in range(1, veces):
    if lista[fin] <= maxx:
        suma += 1
    else:
        while lista[fin] > maxx:
            ini += 1
            suma -= 1
            maxx = lista[ini] +5
        
        suma += 1
    
    c = max(c, suma)

print(c)
            
        
