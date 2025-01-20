# Recibimos la entrada
cant = int(input())
lista = list(map(int, input().split()))
options = {0:[0, 0], 1:[0, 2], 2:[1, 0], 3:[1, 2]}

# Creamos el dp 
dp = [[] for _ in range(cant)]

selec = options[lista[0]]
dp[0] = selec

adicion = {0:1, 1:0, 2:0}

estado = {selec[0]:adicion[selec[0]], selec[1]:adicion[selec[1]]}

# Caso Base
valores = estado.values()

# Llenamos el dp
for i in range(1, cant):
    selec = options[lista[i]]
    dp[i] = selec
    valores = []

    for n in range(2):
        op = float('inf')

        for x in range(2):
            if selec[n] != dp[i-1][x] or selec[n] == 0:
                op = min(op, estado[dp[i-1][x]]+adicion[selec[n]])

        valores.append(op)

    estado[selec[0]] = valores[0]
    estado[selec[1]] = valores[1]
        
print(min(valores))