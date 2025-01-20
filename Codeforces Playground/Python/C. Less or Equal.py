cant, corte = list(map(int, input().split()))
lista = sorted(list(map(int, input().split())))

if corte == cant:
    r = lista[-1]
elif corte == 0:
    r =  lista[0]-1
    if r == 0:
        r = -1
elif corte > cant or lista[corte-1] == lista[corte]:
    r = -1
else:
    r = lista[corte-1]

print(r)