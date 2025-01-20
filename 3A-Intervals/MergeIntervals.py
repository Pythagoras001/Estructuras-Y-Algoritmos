class Solution:
    def mergeIntervals(self, intervals: list[list[int]]):
        lista = intervals
        lista.sort(key=lambda x: x[0])

        fusion = []
        mod = lista[0]

        for i in range(1, len(lista)):
            if mod[1] > lista[i][0]:
                mod[1] = max(mod[1], lista[i][1])
            else:
                fusion.append(mod)
                mod = lista[i]

        fusion.append(mod)
        return(fusion)
    
################################################

def mergeIntervals(intervals):
  sortedIntervals = sorted(intervals, key=lambda x: x[0])
  merged = []
        
  for interval in sortedIntervals:
    if not merged or interval[0] > merged[-1][1]:
      merged.append(interval)
    else:
      merged[-1][1] = max(interval[1], merged[-1][1])

  return merged