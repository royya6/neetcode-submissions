class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bin_search(left, right): 
            while left <= right: 
                m = (left + right) // 2

                if nums[m] == target: return m 
                elif nums[m] < target: 
                    left = m + 1
                else: 
                    right = m - 1
            return -1
 
        l = 0 
        r = len(nums) - 1

        # find pivot 
        while l < r: 
            m = (l + r)//2

            if nums[m] > nums[r]: 
                l = m + 1
            else: 
                r = m 

        pivot = l 

        result = bin_search(0, pivot-1)
        if result != -1: return result 
        
        return bin_search(pivot, len(nums)-1)
        