


estado = dict()
t = 0
maxx = float('-inf')

while(True):

    s = input().split()

    if s[0] == 'fin': break

    if s[0] == 'desliza':
        if not estado.get(s[1], False): 
            t += 1
            estado[s[1]] = True
        else:
            t -= 1
            estado[s[1]] = False

        maxx = max(maxx, t)

    else:
        print(t)

print(maxx)




