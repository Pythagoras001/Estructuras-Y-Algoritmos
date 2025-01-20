class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]):
        order = sorted(intervals, key=lambda x: x[0])

        for i in range(1, len(order)):
            if order[i][0] < order[i-1][1]:
                return(False)
        
        return(True)
    



