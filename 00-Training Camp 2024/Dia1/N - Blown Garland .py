code = input()
colors = 'RBYG'

for i in range(4):
    index = code.index(colors[i]) % 4
    print(code[index::4].count('!'), end=' ')

