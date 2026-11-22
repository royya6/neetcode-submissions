class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # locate row
        i = 0
        while i >= 0 and i < ROWS - 1: 
            curr = matrix[i][0]
            nxt = matrix[i+1][0]

            if curr == target: 
                return True 

            if curr < target and target < nxt:
                break

            i += 1 
                 

        # locate column 
        idx = COLS // 2
        lower, upper = 0, COLS-1

        while lower <= upper: 
            idx = (lower + upper) // 2
            curr = matrix[i][idx] 

            if curr == target:
                return True 

            if curr > target: 
                upper = idx - 1
            else: 
                lower = idx + 1


        return False


        