class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for item in nums: 
            if item in seen: return True 
            else: seen.append(item)

        return False
        