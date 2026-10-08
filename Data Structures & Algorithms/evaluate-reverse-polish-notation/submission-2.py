class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = []
        ops = {"+", "-", "*", "/"}
        res = 0 

        def eval(op, n1, n2): 
            match op: 
                case "+": 
                    return n1 + n2
                case "-": 
                    return n1 - n2
                case "*": 
                    return n1 * n2 
                case "/": 
                    return int(n1 / n2)



        for t in tokens: 
            if t not in ops: 
                s.append(int(t))
            else: 
                n1 = s.pop()
                n2 = s.pop()
                res = eval(t, n2, n1)
                s.append(res)
        
        return s[0]



        