import math 
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()

        # max rate = piles[-1], then time = len(piles)
        
        def eating_time(rate, piles): 
            res = 0 
            for pile in piles: 
                res += math.ceil(pile / rate)
            return res 

        lower, upper = 1, piles[-1]
        res = upper

        while lower <= upper: 
            mid = (lower + upper) // 2
            
            time = eating_time(mid, piles)

            # print(lower, mid, upper, ":", time)

            if time > h: 
                lower = mid + 1
            else: 
                upper = mid - 1
                res = min(res, mid)

            

        return res





        