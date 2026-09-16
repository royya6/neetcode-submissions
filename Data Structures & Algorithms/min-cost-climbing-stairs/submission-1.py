class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # dp[i] = min cost of reaching that step 
        n = len(cost)
        dp = [0]*(n+1)

        for i in range(2, n+1): 
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])

        return dp[n]