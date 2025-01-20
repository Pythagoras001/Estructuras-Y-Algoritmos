estado = input()
c = 1
r = 'NO'

for i in range(1, len(estado)):
    if estado[i-1] == estado[i]:
        c += 1
        
        if c == 7:
            r = 'YES'
            break
    else:
        c = 1

print(r)

