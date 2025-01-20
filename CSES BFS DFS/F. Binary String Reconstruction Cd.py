
# Creamos un Dfs
def dfs(ini, n1, n2, n3):
    c = [ini]
    r = []

    while c:
        act = c.pop()
        print(act, end='')

        if act == 0 and n1 > 0:
            c.append(0)
            n1 -= 1
        elif act == 1 and n3 > 0:
            c.append(1)
            n3 -= 1
        elif n2 > 0:
            if act == 0:
                c.append(1)
            else:
                c.append(0)
                
            n2 -= 1

    return r

# Recibimos la entrada
veces = int(input())

for _ in range(veces):
    n1, n2, n3 = list(map(int, input().split()))
    star = 0
    if n2 + n3 > 0:
        star += 1

    (dfs(star, n1, n2, n3))
    print('')