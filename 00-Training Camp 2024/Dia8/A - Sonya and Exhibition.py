campo, perso = list(map(int, input().split()))

for _ in range(perso):
    a = input()

b = ['0','1'] * ((campo//2)+1)
print(''.join(b[:campo]))