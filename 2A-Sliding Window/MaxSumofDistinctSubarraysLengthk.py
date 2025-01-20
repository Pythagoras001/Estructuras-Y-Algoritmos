class Solution:
    def maxSum(self, nums: list[int], k: int):
        lista = nums
        conjun = k

        inicio = 0
        repe = dict()
        suma = 0
        maxsuma = 0

        for fin in range(len(lista)):
            suma += lista[fin]
            repe[lista[fin]] = repe.get(lista[fin], 0) + 1

            while repe[lista[fin]] > 1 or len(repe) > conjun:
                repe[lista[inicio]] -= 1
                if repe[lista[inicio]] == 0:
                    del repe[lista[inicio]]
                    
                suma -= lista[inicio]
                inicio += 1

            if fin - inicio + 1 == conjun:
                maxsuma = max(maxsuma, suma)

        return(maxsuma)
