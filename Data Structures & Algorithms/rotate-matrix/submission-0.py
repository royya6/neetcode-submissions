import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # reverse row order
        matrix.reverse()

        # print(matrix)
        
        # swap along diagonal 
        for i in range(n): 
            for j in range(i, n): 
                # print(i, j)
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
            

        # print(matrix)
            

        
        