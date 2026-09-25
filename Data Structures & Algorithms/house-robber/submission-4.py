class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        # dp[i] = max money robbed starting at house i
        dp = [0]*n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        currMax = nums[0]

        for i in range(2, n): 
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            print(dp)

        return dp[n-1]