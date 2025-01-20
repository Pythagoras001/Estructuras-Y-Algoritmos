cant = int(input())

lista = list(map(int, input().split()))
lista2 = sorted(lista)

p1 = [0] * (cant+1)
p2 = [0] * (cant+1)

for i in range(1, cant+1):
    p1[i] = p1[i-1] + lista[i-1]
    p2[i] = p2[i-1] + lista2[i-1]

consultas = int(input())

for _ in range(consultas):
    code = list(map(int, input().split()))

    if code[0] == 1:
        print(p1[code[2]] - p1[code[1]-1])
    else:
        print(p2[code[2]] - p2[code[1]-1])