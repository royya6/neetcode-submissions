class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        nums = [] # unique numbers 
        freq = {}

        for cand in candidates: 
            freq[cand] = freq.get(cand, 0) + 1
            if freq[cand] == 1: 
                nums.append(cand)

        def dfs(i, curr, total): 

            if total == target: 
                res.append(curr.copy())
                return 
            
            if total > target or i == len(nums): return 

            if freq[nums[i]] > 0: 
                curr.append(nums[i])
                freq[nums[i]] -= 1

                dfs(i, curr, total + nums[i])

                #backtrack 
                curr.pop()
                freq[nums[i]] += 1

            
            dfs(i+1, curr, total)
        
        dfs(0, [], 0)
        return res 
        