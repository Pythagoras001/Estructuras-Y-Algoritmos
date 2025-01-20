class Solution:
    def maxScore(self, cards: list[int], k: int):
        lista = cards
        conjun = k

        estado  = 0
        maxsuma = 0
        inicio = conjun-1

        for fin in range(conjun-1, (conjun*(-1))-1, -1):
            estado += lista[fin]

            if abs(fin-(inicio+1)) == conjun:
                maxsuma = max(maxsuma, estado)
                estado -= lista[inicio]
                inicio -= 1

        return(maxsuma)
    
###############################################################

def maxScore(cards, k):
    total = sum(cards)
    if k >= len(cards):
        return total

    state = 0
    max_points = 0
    start = 0

    for end in range(len(cards)):
        state += cards[end]

        if end - start + 1 == len(cards) - k:
            max_points = max(total - state, max_points)
            state -= cards[start]
            start += 1

    return max_points