class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        
        def find(coord: (int, int), visited: List[(int, int)], curr: str):

            if curr == word: return True 

            if len(curr) == len(word): return False 

            adj = [(coord[0]-1, coord[1]), (coord[0], coord[1]+1), (coord[0]+1, coord[1]), (coord[0], coord[1]-1)]

            for tile in adj: 
                if 0<=tile[0]<height and 0<=tile[1]<width and tile not in visited:            
                    ch = board[tile[0]][tile[1]]
                    if ch != word[len(curr)]: continue  

                    curr = curr + ch
                    visited.append(tile)

                    if find(tile, visited, curr): return True 
                    curr = curr[:-1]
                    visited.pop()
            
            return False 

        for i in range(height): 
            for j in range(width): 
                if board[i][j] != word[0]: continue 

                if find((i, j), [(i, j)], word[0]): return True 

        return False 