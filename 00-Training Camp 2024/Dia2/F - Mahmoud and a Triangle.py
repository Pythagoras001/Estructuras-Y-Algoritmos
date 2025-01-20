def trianguloValido(num, lista):
    for i in range(num-1, 1, -1):
        iz = 0
        dere = i-1
        top = i

        while iz < dere:
            if lista[dere] + lista[iz] > lista[top]:
                return 'YES'
            else:
                iz += 1
            
    return 'NO'

num = int(input())
lista = sorted(list(map(int, input().split())))

print(trianguloValido(num, lista))
