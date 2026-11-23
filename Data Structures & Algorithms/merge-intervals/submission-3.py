class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by start time
        intervals.sort(key= lambda x: x[0])
        res = []

        start, end = intervals[0]
        for i in range(len(intervals)): 
            next_start, next_end = intervals[i]

            if end >= next_start:
                end = max(end, next_end)
            else:
                res.append([start, end])
                start, end = next_start, next_end

        res.append([start, end])

        return res
