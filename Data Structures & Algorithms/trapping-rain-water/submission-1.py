class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix = [0]*n
        suffix = [0]*n

        prefix[0] = height[0]
        suffix[n-1] = height[n-1]

        for i in range(1, n-1): 
            prefix[i] = max(height[i], prefix[i-1])
            suffix[n-i-1] = max(height[n-i-1], suffix[n-i])

        # print(prefix)
        # print(suffix)

        total = 0 
        for i in range(n): 
            total += max(min(prefix[i], suffix[i]) - height[i], 0) 
            # print(total)

        return total 
            