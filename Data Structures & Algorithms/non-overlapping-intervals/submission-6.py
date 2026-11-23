class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        # sort intervals by end time
        intervals.sort(key= lambda x: x[0])
        res = 0

        start, end = intervals[0]
        for i in range(n-1): 
            next_start, next_end = intervals[i+1]
            if end > next_start: 
                res += 1
                end = min(end, next_end)
            else: 
                end = next_end

        return res
                    