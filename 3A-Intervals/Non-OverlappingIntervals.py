class Solution:
    def nonOverlappingIntervals(self, intervals):
        if not intervals:
            return 0
        
        lista = intervals
        lista.sort(key=lambda x: x[1])

        contador = 1
        fin = lista[0][1]

        for i in range(1, len(lista)):
            if lista[i][0] > fin:
                fin = lista[i][1]
                contador += 1

        return(len(lista) - contador)