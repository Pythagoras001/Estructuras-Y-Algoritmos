# Creamos el dfs
def dfs(ini):
    cola = [(ini, 0)]
    r = 1
    while cola:
        act, camb = cola.pop()

        if camb == cant:
            r = min(r, act)
            continue

        cola.append(((act+mov[camb])%360, camb + 1))
        cola.append((((act-mov[camb])+360)%360, camb + 1))

    return r

# Recibimos la entrada
cant = int(input())
mov = []

for _ in range(cant):
    mov.append(int(input()))

# Aplicamos el dfs
r = 'NO'
if not dfs(0):
    r = 'YES'

print(r)