'''
Se llama top down porque vamos del caso mas grande y lo
reducimos a los casos base en este problema los reducimos 
al fiboo de 1 y 0
'''

def fiboo(n):

    if memory[n] != -1: # Si visitamos un arbol ya visto retornamos la respuesta y ya
        return memory[n]
    
    if n < 2: # Definimos los casos base en esta situacion 1 y 0
        return 1
    
    aws = fiboo(n-1) + fiboo(n-2) # Hacemos la llamada recursiva
    memory[n] = aws # Guardamos en memoria la respuesta de los arboles vistos
    return aws

n = int(input())

# Creamos una memoria para no recorrer arboles ya vistos
memory = [-1]*(n+1)

fiboo(n) # llamamos la funcion

print(memory)