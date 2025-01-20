class Solution:
    def longestSubstringWithoutRepeat(self, s: str):
        lista = list(s)

        inicio = 0
        estado = dict()
        maxestado = 0

        for fin in range(len(lista)):
            estado[lista[fin]] = estado.get(lista[fin], 0) + 1

            while estado[lista[fin]] > 1:
                estado[lista[inicio]] -= 1
                inicio += 1

            maxestado = max(maxestado, fin - inicio+1)

        return(maxestado)