cant = int(input())
lista = sorted(list(map(int, input().split())))

c = 0

for i in range(1, cant+1):
    c += abs(i - lista[i-1])

print(c)