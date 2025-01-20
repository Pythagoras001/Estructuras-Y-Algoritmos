lista = [[[2,4],[7,10]],[[1,5]],[[6,9]]]
inter = [i for times in lista for i in times]
inter.sort(key=lambda x: x[0])

unifi = []

for intervalo in inter:
    if not unifi or intervalo[0] > unifi[-1][1]:
        unifi.append(intervalo)
    else:
        unifi[-1][1] = max(unifi[-1][1], intervalo[1])

libre = []

for i in range(1, len(unifi)):
    libre.append([unifi[i-1][1], unifi[i][0]])

print(libre)