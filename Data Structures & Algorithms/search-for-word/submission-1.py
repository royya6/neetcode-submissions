class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        
        def find(r, c, i):

            if i == len(word): return True 

            if (r<0 or c<0 or r>=height or c>=width or 
                word[i] != board[r][c] or board[r][c] == '#'): 
                return False 

            board[r][c] = '#'
            res = find(r+1, c, i+1) or find(r-1, c, i+1) or find(r, c+1, i+1) or find(r, c-1, i+1) 

            board[r][c] = word[i]

            return res

        for i in range(height): 
            for j in range(width): 
                if board[i][j] != word[0]: continue 

                if find(i, j, 0): return True 

        return False 