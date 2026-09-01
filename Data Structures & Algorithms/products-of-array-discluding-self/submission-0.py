class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroes = 0 

        for num in nums: 
            if num: prod *= num
            else: zeroes += 1

        res = [0]*len(nums)

        if zeroes > 1: return res 

        for i, c in enumerate(nums): 
            if zeroes: 
                if c: res[i] = 0 
                else: res[i] = prod 
            else: 
                res[i] = prod // c
        
        return res

    
        
        