'''
Se llama Buttom Up porque vamos de los casos mas peque;os 
(los casos base) a los niveles mas altos en este caso
usamos 1 y 0 como los casos mas peque;os
'''

num = int(input())

dp = [0]*(num+1) # En este tipo trabajamos sobre la memoria
dp[0] = 1 # Asignamos los casos base que escalaran a un valor mas alto
dp[1] = 1

for i in range(2, num+1):
    dp[i] = dp[i-1]+dp[i-2] # los llamamos y asignamos un nuevo valor

print(dp)
