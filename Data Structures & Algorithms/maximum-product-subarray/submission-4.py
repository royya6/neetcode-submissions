class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        # dp[i] = max product subarray ending at index i 
        max_dp, min_dp = [0] * n, [0] * n 

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        for i in range(1, n): 
            curr = nums[i]

            max_dp[i] = max(curr, curr * max_dp[i-1], curr * min_dp[i-1]) 
            min_dp[i] = min(curr, curr * max_dp[i-1], curr * min_dp[i-1]) 

            # print(max_dp)
            # print(min_dp, "\n")


        return max(max_dp)


        