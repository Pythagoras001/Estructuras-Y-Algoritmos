veces = int(input())

for _ in range(veces):
    cant = int(input())
    lista = sorted(list(map(int, input().split())))

    r = []
    
    dere = (cant // 2) + (cant % 2)
    iz = dere-1 

    while iz >= (cant % 2):
        r.append(lista[iz])
        r.append(lista[dere])
        
        iz -= 1
        dere += 1

    if cant % 2 != 0:
        print(*r ,lista[0])
    else:
        print(*r)