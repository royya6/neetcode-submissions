class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        seen = set()
        for char in s:
            if char not in seen:
                if s.count(char) != t.count(char): return False 
                seen.add(char)
        
        return True
        