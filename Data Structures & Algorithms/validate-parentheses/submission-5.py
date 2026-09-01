class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bopen = {'(': ')', '{': '}', '[': ']'}

        for b in s: 
            if b in bopen: 
                stack.append(b)
            else: 
                if not stack: return False 

                top = stack.pop()
                if b != bopen[top]: return False 
        
        return stack == []

        