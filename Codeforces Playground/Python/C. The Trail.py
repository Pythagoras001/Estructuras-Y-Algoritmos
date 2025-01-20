# Creamos 2 funciones par sumar x y y
def sumx(y):
    return sum(tablero[y])

def sumy(x):
    suma = 0
    for piso in tablero:
        suma += piso[x]
    return suma

for _ in range(int(input())):
    # Recibimos la entrada
    n, m = map(int, input().split())
    ruta = input()
    tablero = []

    for _ in range(n):
        tablero.append(list(map(int, input().split())))

    # Guardamos las coordenadas del camino
    camino = [[0,0]]
    y = 0
    x = 0

    for i in range(len(ruta)):
        if ruta[i] == 'D':
            y += 1
        else:
            x += 1
        camino.append([y, x])

    # Iteramos sobre las casillas para modificar
    for i in range(len(ruta)):
        y, x = camino[i]
    
        if y < camino[i+1][0]:
            tablero[y][x] = -sumx(y)
        else:
            tablero[y][x] = -sumy(x)  

    tablero[-1][-1] = -sumx(-1)

    # Imoprimimos respuesta
    for fila in tablero:
        print(*fila)