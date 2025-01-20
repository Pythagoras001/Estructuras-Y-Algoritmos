veces = int(input())

for _ in range(veces):
    size = input()
    code = input()

    a = ''
    b = ''
    may = False

    for num in code:
        if num == '0':
            a += '0'
            b += '0'

        if may:
            a += '0'
            if num == '2':
                b += '2'
            elif num == '1':
                b += '1'
        else:
            a += '1'
            if num == '2':
                b += '1'
            elif num == '1':
                b += '0'
                may = True

    print(a)
    print(b)


