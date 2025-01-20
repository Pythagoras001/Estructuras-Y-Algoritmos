lista = input()

pila = []
letra = ''
num = 0

for i in range(len(lista)):
    if lista[i] == '[':
        pila.append(letra)
        pila.append(num)
        letra = ''
        num = 0
    
    elif lista[i] == ']':
        n = pila.pop()
        letraPasasa = pila.pop()
        letra = letraPasasa + letra*n 

    elif lista[i].isdigit():
        num = num*10 + int(lista[i])

    else:
        letra += lista[i]

print(letra)

