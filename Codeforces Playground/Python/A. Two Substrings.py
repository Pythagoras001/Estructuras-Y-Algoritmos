code = input()

fin = len(code)-1
ini = fin -1

c = 0
p1 = True
p2 = True

while ini >= 0:
    if code[ini]+code[fin] == 'AB' and p1:
        c += 1
        p1 = False
        ini -= 2
        fin -= 2
    
    elif code[ini]+code[fin] == 'BA' and p2:
        c += 1
        p2 = False
        ini -= 2
        fin -= 2
    else:
        ini -= 1
        fin -= 1

    if c == 2:break

print('NO' if c < 2 else 'YES')
   