class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end 
        intervals.sort(key= lambda x: x[1])

        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)): 
            if intervals[i][0] < prevEnd: 
                res += 1
            else: 
                prevEnd = intervals[i][1]

        return res         