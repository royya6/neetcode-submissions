class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = {r : set() for r in range(9)} # rows[r] = seen digits in row 
        cols = {c : set() for c in range(9)}
        squares = {(r, c): set() for r in range(3) for c in range(3)} # squares[(r//3, c//3)] = seen in square 

        for i in range(9): 
            for j in range(9): 

                curr = board[i][j]
                if curr == ".": continue 

                if curr in rows[i]: return False 
                else: 
                    rows[i].add(curr)

                if curr in cols[j]: return False
                else: 
                    cols[j].add(curr)
                
                if curr in squares[(i//3, j//3)]: return False 
                else: 
                    squares[(i//3, j//3)].add(curr)

        return True 