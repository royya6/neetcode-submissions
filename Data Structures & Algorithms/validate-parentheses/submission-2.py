class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bopen = {'(': ')', '{': '}', '[': ']'}

        for b in s: 
            if b in bopen: 
                stack.append(b)
            else: 
                if len(stack) == 0: return False 

                top = stack.pop()
                if b != bopen[top]: return False 
        
        return stack == []

        