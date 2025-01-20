class Solution:
    def characterReplacement(self, s: str, k: int):
        lista = list(s)
        cupos = k

        inicio = 0
        estado = dict()
        maxestado = 0
        maxfrecuencia = 0

        for fin in range(len(lista)):
            estado[lista[fin]] = estado.get(lista[fin], 0) + 1
            maxfrecuencia = max(maxfrecuencia, estado[lista[fin]])

            while maxfrecuencia + cupos < fin - inicio+1:
                estado[lista[inicio]] -= 1
                inicio += 1

            maxestado = max(maxestado, fin - inicio+1)

        return(maxestado)