class Solution:
    def dailyTemperatures(self, temps: list[int]):
        lista = temps

        pila = []
        base = [0] * len(lista)

        for i in range(len(lista)):
            while pila and lista[i] > lista[pila[-1]]:
                index = pila.pop()
                base[index] = i - index
            pila.append(i)

        return(base)
