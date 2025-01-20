class Solution:
    def isValid(self, s: str) -> bool:
        lista = s
        pila = []
        dicc = {')':'(',']':'[','}':'{'}
       
        for char in lista:
            if char in dicc:
                if not pila or dicc[char] != pila[-1]:
                    return False
                pila.pop()
            else:
                pila.append(char)

        return len(pila) == 0
    
solucion = Solution
print(solucion.isValid(solucion, '{}'))



