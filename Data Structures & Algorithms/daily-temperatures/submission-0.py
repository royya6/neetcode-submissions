class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # dp[i] = number of days after i before warmer temp
        n = len(temperatures)
        dp = [0] * n
        stack = [0]

        for i in range(1, n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous = stack.pop()
                dp[previous] = i - previous

            stack.append(i)

            

        return dp


