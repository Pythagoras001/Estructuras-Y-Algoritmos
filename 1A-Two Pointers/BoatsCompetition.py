for _ in range(int(input())):

    cant = int(input())
    lista = sorted(list(map(int, input().split())))
    dicc = {0:0}

    for dere in range(len(lista)-1, 0, -1):
       
        for iz in range(dere):
            suma = lista[iz] + lista[dere]
            
            if suma not in dicc:
                dicc[suma] = 0

                i = 0
                d = len(lista)-1

                while i < d:
                    if lista[i] + lista[d] == suma:
                        dicc[suma] += 1
                        i += 1
                        d -= 1
                    elif lista[i] + lista[d] > suma:
                        d -= 1
                    else:
                        i += 1

    print(max(dicc.values()))
