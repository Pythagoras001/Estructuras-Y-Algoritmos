lista = list(map(int, input().split()))
r = min(lista[0], lista[2], lista[3]) * 256
print(r + min(lista[0]-(r//256), lista[1]) * 32)