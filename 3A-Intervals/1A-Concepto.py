def nonOverlappingIntervals(intervals):
  if not intervals:
    return 0

  intervals.sort(key=lambda x: x[1])
  print(intervals)
  end = intervals[0][1]
  count = 1

  for i in range(1, len(intervals)):
    # Non-overlapping interval found
    if intervals[i][0] >= end:
      end = intervals[i][1]
      count += 1

  return len(intervals) - count


print(nonOverlappingIntervals([[1,2],[11,17],[2,18],[7,10]]))