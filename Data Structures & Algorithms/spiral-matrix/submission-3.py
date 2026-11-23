import math
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []

        while matrix: 
            # top row
            res.extend(matrix.pop(0))

            # right side
            for row in matrix:
                if row:
                    res.append(row.pop())

            # bottom row
            if matrix: 
                res.extend(matrix.pop()[::-1])

            # left side 
            for row in reversed(matrix):
                if row:
                    res.append(row.pop(0))

        return res

        