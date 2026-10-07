class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)
        
        # check rows and cols 
        for i in range(n): 
            seenRow = set()
            seenCol = set()
            for j in range(n):
                rowDigit = board[i][j]
                colDigit = board[j][i]

                if rowDigit in seenRow: 
                    # print(rowDigit, seenRow)
                    return False 
                elif rowDigit != "." : 
                    seenRow.add(rowDigit)

                if colDigit in seenCol: 
                    # print(colDigit, seenCol)
                    return False 
                elif colDigit != "." : 
                    seenCol.add(colDigit)

        # check squares 
        def checkSubSquare(r, c): 
            seen = set()
            for i in range(r, r+3): 
                for j in range(c, c+3): 
                    # print(i, j)
                    curr = board[i][j]

                    if curr in seen: 
                        # print(curr, seen)
                        return False 
                    elif curr != ".": seen.add(curr)

            return True 

        for i in range(0, 9, 3): 
            for j in range(0, 9, 3): 
                if not checkSubSquare(i, j): 
                    # print(i, j)
                    return False 


        return True 