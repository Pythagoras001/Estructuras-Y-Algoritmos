class Solution:
    def threeSum(self, nums: list[int]):
        lista = sorted(nums)
        conjun = []

        for i in range(len(lista)-1, 1, -1):
            iz = 0
            dere = i - 1 
            maxx = lista[i]

            while iz < dere:
                if lista[iz] + lista[dere] + maxx > 0:
                    dere -= 1
                elif lista[iz] + lista[dere] + maxx < 0:
                    iz += 1
                else:
                    g = ([lista[iz], lista[dere], maxx])
                    
                    if g not in conjun:
                        conjun.append(g)
                    break

        return list(conjun)

