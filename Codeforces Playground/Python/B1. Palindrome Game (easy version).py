veces = int(input())

for _ in range(veces):
    cant = int(input())
    code = input()
    cero = code.count('0')

    r = 'BOB'
    if cero % 2 != 0 and cero > 1:
        r = 'ALICE'

    print(r)
