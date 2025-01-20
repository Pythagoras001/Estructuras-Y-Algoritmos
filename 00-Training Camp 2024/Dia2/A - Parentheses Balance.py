def cadena_valida(code):
    pila = []
    dicc = {']':'[', ')':'('}

    for chart in code:
        if chart not in dicc:
            pila.append(chart)
        else:
            if not pila or dicc[chart] != pila[-1]:
                return False
            pila.pop()
    
    return len(pila) == 0



veces = int(input())

for _ in range(veces):
    code = input()
    r = 'No'

    if cadena_valida(code):
        r = 'Yes'
    
    print(r)

