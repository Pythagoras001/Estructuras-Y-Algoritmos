

for _ in range(int(input())):
    n = int(input())

    gustos = []

    vistosH = [0]*n
    vistosM = [0]*n

    noEmpa = []


    for _ in range(n):
        lista = sorted(list(map(int, input().split()))[1:])

        gustos.append(lista)


    for i in range(n):
        for index in gustos[i]:
            if not vistosH[index-1]:
                vistosH[index-1] = 1
                vistosM[i] = 1
                break
        if not vistosM[i]:
            noEmpa.append(i+1)

    if not len(noEmpa):
        print("OPTIMAL")
    else:
        print("IMPROVE")
        k = 0

        for i in range(len(noEmpa)):
            print(noEmpa[i], end=' ')
            while(k < n):
                if not vistosH[k]:
                    print(k+1)
                    break
                k += 1
            

