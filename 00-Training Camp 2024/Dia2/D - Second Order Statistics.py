cant = int(input())
lista = list(map(int, input().split()))

minn = lista[0]
sigui = max(lista)

for num in lista:
    if minn > num:
        sigui = minn
        minn = num
    else:
        if num > minn:
            sigui = min(sigui, num)

if minn == sigui : sigui = 'NO'
print(sigui)