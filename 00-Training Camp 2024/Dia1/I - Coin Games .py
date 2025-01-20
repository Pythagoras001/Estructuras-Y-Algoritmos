veces = int(input())

for _ in range(veces):
    cant = int(input())
    code = input()
    c = 0
    r = 'NO'

    for letter in code:
        if letter == 'U':
            c += 1
    
    if c % 2 != 0:
        r = 'YES'

    print(r)