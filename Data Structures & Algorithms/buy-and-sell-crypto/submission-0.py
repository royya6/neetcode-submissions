class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = prices[0]

        for i in range(len(prices)): 
            if prices[i] < bought: 
                bought = prices[i]
            else:
                profit = max(profit, prices[i]-bought)

        return profit
                