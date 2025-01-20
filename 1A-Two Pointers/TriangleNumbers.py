class Solution:
    def triangleNumber(self, heights: list[int]):
        lista = sorted(heights)
        conta = 0

        for i in range(len(lista)-1, 1, -1):
            iz = 0
            dere = i-1
            top = lista[i]

            while iz < dere:
                if lista[iz] + lista[dere] > top:
                    conta += dere - iz
                    dere -= 1
                
                else:
                    iz += 1
    
        return conta