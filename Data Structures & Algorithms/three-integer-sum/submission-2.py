class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for l, a in enumerate(nums): 

            if a > 0: break 

            #skip duplicates 
            if l > 0 and a == nums[l-1]: continue 

            m, r = l + 1, len(nums)-1

            while m < r: 
                currSum = a + nums[m] + nums[r]

                if currSum == 0: 
                    res.append([a, nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while nums[m] == nums[m - 1] and m < r:
                        m += 1

                elif currSum > 0: 
                    r -= 1
                else: 
                    m += 1            

        return res 
        