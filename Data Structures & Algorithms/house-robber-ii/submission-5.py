class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1: return nums[0]
        if n == 2: return max(nums)
        n -= 1

        nums1 = nums[1:]
        nums2 = nums[:-1]

        #dp[i] = max money robbed at house i 
        dp1, dp2 = [0]*n, [0]*n

        dp1[0] = nums1[0]
        dp1[1] = max(dp1[0], nums1[1])

        dp2[0] = nums2[0]
        dp2[1] = max(dp2[0], nums2[1])

        for i in range(2, n): 
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums1[i])
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums2[i])

        return max(dp1[n-1], dp2[n-1])