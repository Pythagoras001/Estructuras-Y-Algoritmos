cant, pre = map(int, input().split())
lista = list(map(int, input().split()))

dicc = dict()
vistos = set()
c = 0

for i in reversed(range(cant)):
    if lista[i] not in vistos:
        c += 1
        vistos.add(lista[i])
    dicc[i] = c

for _ in range(pre):
    print(dicc[int(input())-1])