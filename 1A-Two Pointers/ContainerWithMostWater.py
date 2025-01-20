class Solution:
    def max_area(self, alturas):
        maxx = 0
        izq = 0
        dere = len(alturas)-1

        while izq < dere:

            minn = min(alturas[izq], alturas[dere])
            maxx = max(maxx, minn*(dere-izq))

            if alturas[izq] < alturas[dere]:
                izq += 1
            else:
                dere -= 1
        
        return maxx