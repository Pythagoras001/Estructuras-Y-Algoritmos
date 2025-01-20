cant, fin = list(map(int, input().split()))
lista = list(map(int, input().split()))
lista.append(fin)

e = lista[0]
a = 0

for i in range(1, cant+1):
    if i % 2 != 0:
        a += lista[i] - lista[i-1]
    else:
        e += lista[i] - lista[i-1] 

print(max(a + lista[0]-1, e))