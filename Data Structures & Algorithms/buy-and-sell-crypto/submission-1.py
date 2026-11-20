class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minBuy = prices[0]
        maxP = 0

        for p in prices: 
            minBuy = min(minBuy, p)
            maxP = max(maxP, p - minBuy)

        return maxP
